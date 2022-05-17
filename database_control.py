import os
import sqlite3
from penguin import User

directory = 'database.db'

#os.remove(directory)

connection = sqlite3.connect(directory)
#cursor = connection.cursor()

#cursor.execute("DELETE FROM cards_1")
#cursor.execute(f"CREATE TABLE cards_1 (amount INTEGER);")
#connection.commit()
user = User('Wissens#1115', connection)
user.add_card(1)


# with open('cards.txt', 'r') as file:
#     info = file.readlines()

#     for card in info:
#         elements = card.split('-')
#         cursor.execute(f"INSERT INTO card_catalog VALUES ('{elements[1]}',{elements[0]},{elements[3]},'{elements[2]}','{elements[4]}')")
#         connection.commit()

# cursor.execute("""CREATE TABLE members (
#             user TEXT,
#             score INTEGER,
#             money INTEGER
#         );""")

# cursor.execute("""CREATE TABLE card_catalog (
#             name TEXT,
#             number INTEGER,
#             value INTRGER, 
#             element TEXT,
#             color TEXT
#         );""")

connection.close()