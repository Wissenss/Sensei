import sqlite3 
import os

connection = sqlite3.connect('database.db')
records = connection.cursor()

def set_records():
    records.execute("""CREATE TABLE records (
        user TEXT,
        score INTEGER,
        money INTEGER
    )""")
    connection.commit()

def set_cards_catalog():
    records.execute("""CREATE TABLE cards_catalog (
        number INTEGER,
        value INTRGER, 
        element TEXT,
        color TEXT,
        image BLOB
    )""")
    connection.commit()

def delete_table(table):
    try:
        records.execute(f"DROP TABLE {table}")
        connection.commit
    except Exception:
        print(f"table \"{table}\" does not exist")

#os.remove('database.db')

delete_table("records")
delete_table("cards_catalog")
set_records()
set_cards_catalog()

connection.close()
print('records.db database has been reset, all data was deleted')