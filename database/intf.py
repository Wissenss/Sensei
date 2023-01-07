import sqlite3
import logging
from errors import ErrorCode

if __name__ != "__main__":
    from database.dataModule import DataModule
    import logger
else:
    from dataModule import DataModule
    from .. import logger

# def DataModuleOperation(operationFunction):
#     def wrapper(*args, **kwargs):
#         connection = DataModule()
#         cursor = connection.cursor()
#         error = ErrorCode.ERR_NO_ERROR

#         operationFunction(cursor=cursor, )

#         return error

#player queries
# @DataModuleOperation
def add_player(discordId, score=0, capital=0):
    connection = DataModule()
    cursor = connection.cursor()
    error = ErrorCode.ERR_NO_ERROR
    playerRecord = []

    #check if player exists
    cursor.execute("SELECT * FROM Players WHERE discordId = ?", (f"{discordId}",))

    #if not, create new
    if not(cursor.fetchall()):
        cursor.execute("INSERT INTO Players(discordId, score, capital) VALUES(?, ?, ?)", (f"{discordId}", score, capital))
        playerRecord = [discordId, score, capital]
        connection.commit()
        connection.close()
    else:
        connection.close()
        error = ErrorCode.ERR_RECORD_ALREADY_EXISTS_PLAYERS

    return error, playerRecord

def update_player(**kwargs):
    pass
    
def get_player(discordId):
    #the player record return has the following structure:
    #record[0] = rowId
    #record[1] = discordId
    #record[2] = score
    #record[3] = capital

    connection = DataModule()
    cursor = connection.cursor()
    error = ErrorCode.ERR_NO_ERROR

    cursor.execute("SELECT * FROM Players WHERE discordId = ?", (f"{discordId}",))

    playerRecord = cursor.fetchone()
    if not(playerRecord):
        error = ErrorCode.ERR_RECORD_NOT_FOUND_PLAYERS

    return error, playerRecord