import sqlite3
import logging
import os
from errors import ErrorCode

if __name__ != "__main__":
    from database.dataModule import DataModule
    import logger
else:
    from dataModule import DataModule
    from .. import logger

"""
utilities
"""
import time
size = os.get_terminal_size()
width = int(size.columns/2)
def cardsProgressBar(progress, total):
    ratio = progress / float(total)
    barwidth = width * ratio
    bar = "\033[0m■\033[0m"* int(barwidth) + "-" * (width - int(barwidth))
    print(f"\r   |{bar}| {progress}/{total}", end="\r")
    # █
    # print(f"\r   {bar} {ratio*100:.2f}%", end="\r")
    # print(f"\r    filling... Card: test\n    |{bar}| {progress}/{total}", end="\r")
    # time.sleep(0.1)

"""
This script will create a new database if unexistent
and add missing records to default tables
"""
#conect to database
connection = DataModule()
cursor = connection.cursor()

#Players
try:
    print(f"\n creating table \033[36mPlayers\033[0m...", end="\t")
    query = "CREATE TABLE Players(discordId TEXT UNIQUE, score INTEGER, capital INTEGER);"
    cursor.execute(query)
    print("\033[42msucces\033[0m", end=" ")
except:
    print("\033[41mskipped\033[0m", end=" ")
    print(": table already exists", end="")
    
#Cards
try:
    print(f"\n creating table \033[36mCards\033[0m...", end="\t")
    query = "CREATE TABLE Cards(cardId INTEGER UNIQUE, name TEXT, element TEXT, value INTEGER, color TEXT);"
    cursor.execute(query)
    print("\033[42msucces\033[0m", end=" ")
    print(" ", end="")
except:
    print("\033[41mskipped\033[0m", end=" ")
    print(": table already exists", end="")

#fill card values
# print(f"\n  filling table \033[36mCards\033[0m...")
print("\n    filling... ")
cards = [
(1, 'cart surfer', 'fire', 3, 'blue'),
(2, 'coffee shop', 'fire', 2, 'green'),
(3, 'astro barrier', 'fire', 8, 'green'),
(4, 'hot chocolate', 'fire', 3, 'orange'),
(5, 'landing pad', 'fire', 4, 'purple'),
(6, 'pizza chef', 'fire', 6, 'purple'),
(7, 'paint by letters', 'fire', 2, 'red'),
(8, 'mine', 'fire', 7, 'red'),
(9, 'construction worker', 'fire', 2, 'yellow'),
(10, 'jet pack adventure', 'fire', 5, 'yellow'),
(11, 'gift shop', 'snow', 3, 'blue'),
(12, 'hiking in the forest', 'snow', 2, 'green'),
(13, 'rescue squad', 'snow', 5, 'green'),
(14, 'pet shop', 'snow', 3, 'orange'),
(15, 'ski village', 'snow', 4, 'purple'),
(16, 'ice hockey', 'snow', 8, 'purple'),
(17, 'ski hill', 'snow', 2, 'red'),
(18, 'snowball fight', 'snow', 6, 'red'),
(19, 'snow forts', 'snow', 2, 'yellow'),
(20, 'soccer', 'snow', 7, 'yellow'),
(21, 'beach', 'water', 3, 'blue'),
(22, 'football', 'water', 5, 'blue'),
(23, 'baseball', 'water', 2, 'green'),
(24, 'emerald princess', 'water', 8, 'green'),
(25, 'bean counters', 'water', 3, 'orange'),
(26, 'manhole cover', 'water', 4, 'purple'),
(27, 'newspaper archives', 'water', 6, 'purple'),
(28, 'underground pool', 'water', 2, 'red'),
(29, 'scuba diving', 'water', 7, 'red'),
(30, 'ice fishing', 'water', 2, 'yellow'),
(31, 'case of the missing coins', 'fire', 2, 'blue'),
(32, 'crates and boxes', 'fire', 5, 'blue'),
(33, 'anvil smith', 'fire', 4, 'green'),
(34, 'halloween', 'fire', 6, 'orange'),
(35, 'knight', 'fire', 3, 'purple'),
(36, 'black puffle', 'fire', 5, 'orange'),
]

progress = 0
succes = 0
cardsProgressBar(progress, len(cards))
for card in cards:
    try:
        cursor.execute("INSERT INTO Cards(cardId, name, element, value, color) VALUES(?,?,?,?,?)", card)
        succes += 1
    except:
        pass

    progress += 1
    cardsProgressBar(progress, len(cards))
print(f"\n    {succes} \033[32msucces\033[0m | {len(cards)-succes} \033[31mskipped\033[0m")

connection.commit()
connection.close()