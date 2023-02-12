"""
Телеграм-бот предназначен для сбора и отражения сведений о стоимости машины Skoda Rapid I от 2014 года на
вторичном рынке Республики Беларусь
"""

from config import API_TOKEN
from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from av_by import get_car_info_list


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Rapid на av.by')
kb.add(b1)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    print('Бот запущен!')
    await bot.send_message(chat_id=message.chat.id,
                           text='Добро пожаловать в бот по поиску цен на Skoda Rapid I!',
                           reply_markup=kb)


@dp.message_handler(lambda message: message.text == 'Rapid на av.by')
async def av_by(message: types.Message):
    await message.reply('Данные с сайта av.by:\nПолучаю данные. Подождите...')

    try:
        car_list = get_car_info_list()
        for car in car_list:  #пока только для четырёх элементов
            car_name = car["car"]
            car_img = car["photo"]
            year = car["year"]
            car_description = car["descriprion"]
            km = car["km"]
            price = car["price"]
            price_usd = car["usd_price"]
            car_url = car["url"]
            location = car["location"]

            photo_caption = f'{car_name}\n{year}\n{car_description}\n{km}\n{price} ({price_usd})\n{car_url}\n{location}'

            await bot.send_photo(chat_id=message.chat.id,
                                 photo=car_img,
                                 caption=photo_caption)

    except Exception as _ex:
        print(_ex)
        await message.answer('Не могу получить данные с сайта av.by...')



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
