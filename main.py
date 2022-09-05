import logging
import menu as nav
from aiogram import Bot, Dispatcher, executor, types
from loguru import logger
from search import *
import book_actions
from forms import *
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
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user_name = types.User.get_current().first_name
    await message.answer(f"Привет, {user_name}\nЯ LibraryThotBot!\nДобро пожаловать в мою билиотеку!",
                                                                                    reply_markup=nav.main_menu)
    request = FormRequest()
    await FormRequest.type_request.set()


@dp.message_handler(state=FormRequest.type_request)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await FormRequest.next()

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Начать новую книгу":
        await bot.send_message(message.from_user.id ,"Хочешь прочитать новую книгу?")

    elif message.text == "Продолжить чтение книги":
        await bot.send_message(message.from_user.id,"Какую книгу мне загрузить?")

    elif message.text == "Удалить книгу из библиотеки":
        await bot.send_message(message.from_user.id,"Какую книгу мне удалить?")

    elif message.text == "Оставить отзыв о книге":
        await bot.send_message(message.from_user.id,"На какую книгу?")

    elif message.text == "Прочитать отзывы о книге":
        await bot.send_message(message.from_user.id,"По какой книге?")

    elif message.text == "Вернуться в главное меню":
        await bot.send_message(message.from_user.id,"Возвращение в главное меню" ,reply_markup=nav.main_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)