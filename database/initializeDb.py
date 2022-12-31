import sqlite3

def initialize(databasePath:str)->None:
    #conect to database
    connection = sqlite3.Connection(databasePath)
    cursor = connection.cursor()

    #init database
    with open("./scripts/init.sql", "r") as file:
        cursor.executescript(file.read())

    connection.commit()
    connection.close()