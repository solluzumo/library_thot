from typing import Dict,Tuple,List
import sqlite3
import grabber

db = sqlite3.connect("thot.db")
sql = db.cursor()
#сохранение книги в бд
def save_book(table: str, columns_values: Dict):
    columns = ', '.join(columns_values.keys())
    values = [tuple(columns_values.values())]
    placeholders = ", ".join("?"*len(columns_values.keys()))
    sql.executemany(f"INSERT INTO {table} "
                    f"({columns}) "
                    f"VALUES ({placeholders})",
                    values)

    db.commit()

#выбор книг из бд
def fetchall(table:str, book_info: str, columns: List[str]) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    sql.execute(f"SELECT {columns_joined} FROM {table} "
                f"where name = '{book_info}' or "
                f"author = '{book_info} or "
                f"genre = '{book_info}'")
    rows = sql.fetchall()
    if len(rows) == 0: #если в бд нет книги, то пытаемся скачать парсером
        if len(grabber.download_book(book_info)) == 0:
            return False

        else:
            sql.execute(
                f"SELECT {columns_joined} FROM {table} "
                f"where name = '{book_info}' or "
                f"author = '{book_info} or "
                f"genre = '{book_info}'")
            rows = sql.fetchall()


    result = []
    for row in rows:
        result.append(row)
    return result


#удаление книг
def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    sql.execute(f"DELETE FROM {table} WHERE ID={row_id}")
    db.commit()
