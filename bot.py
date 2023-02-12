from config import API_TOKEN
from aiogram import Bot, executor, Dispatcher, types


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    print('Бот запущен!')
    await bot.send_message(chat_id=message.chat.id, text='Добро пожаловать в бот по поиску цен на Skoda Rapid I!')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
