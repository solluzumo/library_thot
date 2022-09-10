from typing import Dict,Tuple,List
import sqlite3

db = sqlite3.connect("thot.db")
sql = db.cursor()

def save_book(table: str, columns_values: Dict):
    columns = ', '.join(columns_values.keys())
    values = [tuple(columns_values.values())]
    placeholders = ", ".join("?"*len(columns_values.keys()))
    sql.executemany(f"INSERT INFO {table}"
                    f"({columns})"
                    f"VALUES ({placeholders}),",
                    values)
    db.commit()


