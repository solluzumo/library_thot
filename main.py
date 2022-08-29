import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN =open("token").read()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.answer("Hi!\nI'm LibraryThotBot!\nWelcome to my Library!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)