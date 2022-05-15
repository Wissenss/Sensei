from database import *
import os

directory = 'database.db'
os.remove(directory)

connection = sqlite3.connect(directory)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE members (
            user TEXT,
            score INTEGER,
            money INTEGER
        );""")

cursor.execute("""CREATE TABLE card_catalog (
            number INTEGER,
            value INTRGER, 
            element TEXT,
            color TEXT
        );""")

connection.close()