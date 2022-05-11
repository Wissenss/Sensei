import sqlite3 
import os

def set_records():
    connection = sqlite3.connect('database.db')
    records = connection.cursor()

    records.execute("""CREATE TABLE records (
        user TEXT,
        score INTEGER,
        money INTEGER
    )""")

    connection.commit()
    connection.close()

def set_items():
    connection = sqlite3.connect('database.db')
    records = connection.cursor()

    records.execute("""CREATE TABLE items (
        ID INTEGER,
        name TEXT,
        rank TEXT,
        value INTEGER
    )""")

    connection.commit()
    connection.close()

os.remove('database.db')

set_records()
set_items()

print('records.db database has been reset, all data was deleted')