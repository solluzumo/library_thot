import logging
from search import *
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


logger.add("./db/logs/errors.log",format="{time} {level} {message}",
           level="DEBUG", rotation="10 MB", compression="zip")

API_TOKEN =open("token").read()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user_name = types.User.get_current().first_name
    welcome_text = open("./text/welcome",encoding="utf-8").read()
    await message.answer(welcome_text)

@dp.message_handler(commands=['download'])
async def download_book(message: types.Message):
    if len(message.text.split())>1:
        await message.answer(f"Результаты поиска: {book_search(message.text.split('/download')[1].strip())}")
    else:
        await message.answer("Пожалуйста, после комманды /download введите название, автора или жанр книги")

@dp.message_handler(commands=['feedback'])
async def leave_review(message: types.Message):
    # await message.answer("Мы собираем отзывы со различных ресурсов, с полным списком ресурсов мы можете ознакомиться,"
    #                      "введя комманду /resources")
    if len(message.text.split()) > 1:
        await message.answer(f"По вашему запросу найдены следующие отзывы:{book_search(message.text.split('/feedback')[1].strip())}")
    else:
        await message.answer("Пожалуйста, после комманды /feedback введите название книги")
@dp.message_handler(commands=['review'])
async def read_review(message: types.Message):
    await message.answer("Введи название книги")

    pass
@dp.message_handler(commands=['random'])
async def random_book(message: types.Message):
    pass
@dp.message_handler(commands=['recommended'])
async def recommended_book(message: types.Message):
    await message.answer("Основываясь на запрашиваемых для скачивания книгах и отзывах, я подобрал следующий список:")
    pass



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)