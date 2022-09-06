import logging
from fsm import *
from search import *
from aiogram import Bot, Dispatcher, executor, types
from loguru import logger
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
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
    await message.answer(f"Привет, {user_name}\nЯ LibraryThotBot!\nДобро пожаловать в мою билиотеку!\n\n"
                         f"Комманды:\n"
                         f"Чтобы скачать книгу, введите комманду /download и название или имя автора или жанр книги\n"
                         f"Чтобы оставить отзыв о книге, введите комманду /feedback и название книги\n"
                         f"Чтобы прочитать отзывы о книге, введите комманду /review и название книги\n"
                         f"Чтобы скачать случайную книгу, введите /random\n"
                         f"Чтобы ознакомиться с рекомендуемыми книгами, введите комманду /recommended\n")

@dp.message_handler(commands=['download'])
async def download_book(message: types.Message):
    # await message.answer("Мы загружаем книги со множества различных ресурсов, с полным списком ресурсов мы можете "
    #                      "ознакомиться, введя комманду /resources")
    if len(message.text.split())>1:
        await message.answer(f"По вашему запросу найдены книги: {book_search(message.text.split('/download')[1].strip())}")
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