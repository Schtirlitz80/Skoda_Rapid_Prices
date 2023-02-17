"""
Телеграм-бот предназначен для сбора и отражения сведений о стоимости машины Skoda Rapid I от 2014 года на
вторичном рынке Республики Беларусь
"""

from config import API_TOKEN
from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from av_by import get_cars_info_list
from database import put_list_into_db

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Rapid на av.by')
kb.add(b1)

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='Все объявления', callback_data='av_by_all')
ib2 = InlineKeyboardButton(text='Только новые', callback_data='av_by_new')
ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    print('Бот запущен!')
    await bot.send_message(chat_id=message.chat.id,
                           text='Добро пожаловать в бот по поиску цен на Skoda Rapid I!',
                           reply_markup=kb)


@dp.message_handler(lambda message: message.text == 'Rapid на av.by')
async def av_by(message: types.Message):
    await message.reply('Автомобили Skoda Rapid I начиная с 2014 года на вторичном рынке Республики Беларусь с сайта av.by. Какие объявления показать?',
                        reply_markup=ikb)


@dp.callback_query_handler()
async def av_by_all(callback: types.CallbackQuery):
    if callback.data == 'av_by_all':
        await callback.answer('Данные с сайта av.by ПО ВСЕМ машинам:\nПолучаю данные. Подождите...')
        try:
            car_list = get_cars_info_list()
            put_list_into_db(car_list)  #помещаем данные в базу данных (чтобы потом отличать новые)
        except Exception as _ex:
            print(_ex)
            await callback.answer('Не могу получить данные с сайта av.by...')

    elif callback.data == 'av_by_new':
        await callback.answer('Данные с сайта av.by ПО НОВЫМ объявлениям:\nПолучаю данные. Подождите...')
        try:
            car_list = get_cars_info_list()
            new_car_lst = put_list_into_db(car_list)  # помещаем данные в базу данных (чтобы потом отличать новые)
            car_list = new_car_lst
        except Exception as _ex:
            print(_ex)
            await callback.answer('Не могу получить данные с сайта av.by...')

    if len(car_list) == 0:
        await bot.send_message(chat_id=callback.from_user.id,
                                text='Новые объявления не появились...')
        print('НЕТ НОВЫХ ОБЪЯВЛЕНИЙ!')
        return

    for car in car_list:
        car_name = car["car"]

        car_img = car["photo"]
        print(car_img)

        car_year = car["year"]
        car_description = car["description"]
        km = car["km"]
        price = car["price"]
        price_usd = car["usd_price"]
        car_url = car["url"]
        location = car["location"]

        photo_caption = f'{car_name}\n{car_year}\n{car_description}\n{km}\n{price} ({price_usd})\n{car_url}\n{location}'

        if car_img != "No image":
            await bot.send_photo(chat_id=callback.from_user.id,
                                 photo=car_img,
                                 caption=photo_caption)
        else:
            await callback.answer(photo_caption)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
