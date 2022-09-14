from typing import Dict,Tuple,List
import sqlite3
import grabber

db = sqlite3.connect("thot.db")
sql = db.cursor()

def save_book(table: str, columns_values: Dict):
    columns = ', '.join(columns_values.keys())
    values = [tuple(columns_values.values())]
    placeholders = ", ".join("?"*len(columns_values.keys()))
    sql.executemany(f"INSERT INTO {table} "
                    f"({columns}) "
                    f"VALUES ({placeholders})",
                    values)

    db.commit()

#/get-file/f3c57a85-92f5-458a-9e43-a2a9a22acd79?format=fb2.zip
#/get-file/b9bcba65-5665-4aa3-b393-a1887b2e4db0?format=fb2.zip

def fetchall(table:str, book_info: str, columns: List[str]) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    sql.execute(f"SELECT {columns_joined} FROM {table} "
                f"where name = '{book_info}' or "
                f"author = '{book_info} or "
                f"genre = '{book_info}'")
    rows = sql.fetchall()
    if len(rows) == 0:
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

def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    sql.execute(f"DELETE FROM {table} WHERE ID={row_id}")
    db.commit()
