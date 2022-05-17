#   WARNING!
# By running this script ...
# you will delete all user data on the database

from members import Members
from catalog import Catalog, CardCatalog
import sqlite3
import os

def reset():
    database = 'database.db'

    try:
        os.remove(database)
    except: pass

    connection = sqlite3.connect(database)

    members = Members(connection)
    members.members_create()
    cards = CardCatalog(connection)
    cards.catalog_create()
    cards.catalog_load()

    connection.close()

confirmation = 'Club Penguin'

confirm = input(f"\
Type {confirmation} to delete all user data\n \
catalogs will be restore from Assets/load/ files\n \
:")

keep = True

while keep:
    if confirm == confirmation:
        reset()
        print("Done! all user data has been removed")
        keep = False
    elif confirm == "Exit":
        keep = False
    else:
        confirm = input(f"\
        Wrong frase! remember, type \"{confirmation}\"\n\
        typing \"Exit\" will end the script \
        :")