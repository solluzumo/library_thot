import logging
from typing import List

from search import *
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import db
import grabber

logger.add("./db/logs/errors.log",format="{time} {level} {message}",
           level="DEBUG", rotation="10 MB", compression="zip")

API_TOKEN =open("token").read()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    welcome_text = open("./text/welcome",encoding="utf-8").read()
    await message.answer(welcome_text)


#Функция выбора данных(любых) одной или несколько книг из БД
async def get_data(message: types.Message, command:str, columns: List[str]):
    if len(message.text.split())>1:
        datas = db.fetchall("book", message.text.split(f"/{command}")[1],columns)

    else:
        await message.answer(f"Пожалуйста, после комманды /{command} введите название, имя автора или жанр книги")


#Загрузка файла книги в чат к пользователю
@dp.message_handler(commands=['download'])
async def download_book(message: types.Message):
    book_datas = get_data(message, "download",["name","author","file_path"])
    if len(book_datas) == 0:
        return message.answer("Мне ничего не удалось найти по вашему запросу")
    for index,file in enumerate(book_datas):
        await message.answer(f"{index}. {file[0]} {file[1]}")
        await message.reply_document(open(f"./db/books_files/{file[2]}"), "rb")



#Загрузка отзывов о книге
@dp.message_handler(commands=['reviews'])
async def read_review(message: types.Message):
    path = get_data(message, "reviews", ["reviews_path"])
    reviews = [i for i in open(f"{path}").read().split("\n") if i!= ""]
    for review in reviews:
        await message.answer(review)

#Оставить отзыв о книге
@dp.message_handler(commands=['feedback'])
async def leave_review(message: types.Message):
    await message.answer("Введи название книги")

    pass
#Случайная книга
@dp.message_handler(commands=['random'])
async def random_book(message: types.Message):
    pass
#Рекомендации
@dp.message_handler(commands=['recommended'])
async def recommended_book(message: types.Message):
    await message.answer("Рекомендую к прочтению: ")
    pass



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)