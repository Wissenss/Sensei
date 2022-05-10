import sqlite3 
import os

os.remove('records.db')

connection = sqlite3.connect('records.db')
c = connection.cursor()

c.execute("""CREATE TABLE records (
    user TEXT,
    score INTEGER,
    money INTEGER
)""")

connection.commit()
connection.close()

print('records.db database has been reset, all data was deleted')