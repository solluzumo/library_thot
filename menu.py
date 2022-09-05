from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

#!!!!!!Оптимизировать

#---Main menu buttons---

bttn_start_new_book = KeyboardButton(text="Начать новую книгу")
bttn_cont_reading = KeyboardButton(text="Продолжить чтение книги")
bttn_execute_book = KeyboardButton(text="Удалить книгу из библиотеки")
bttn_leave_review = KeyboardButton(text="Оставить отзыв о книге")
bttn_read_review = KeyboardButton(text="Прочитать отзывы о книге")


#---Main menu---
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(bttn_start_new_book,bttn_cont_reading,bttn_execute_book,
                                                                                bttn_leave_review,bttn_read_review)


#---Back to main menu button---
bttn_back_to_main_menu = KeyboardButton(text="Вернуться в главное меню")


#---New book menu---
bttn_find_new_book_by_name = KeyboardButton(text="Найти книгу по названию")
bttn_find_new_book_by_genre = KeyboardButton(text="Найти книгу по жанру")
bttn_find_new_book_by_author = KeyboardButton(text="Найти книгу по автору")
new_book_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(bttn_find_new_book_by_name,bttn_find_new_book_by_genre,
                                                                bttn_find_new_book_by_author, bttn_back_to_main_menu)



