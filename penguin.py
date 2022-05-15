import sqlite3

class Penguin:
    def __init__(self, username, connection):
        self.user = username
        self.connection = connection
        self.cursor = self.connection.cursor()
        if not self.exist():
            self.cursor.execute(f"INSERT INTO members VALUES ('{self.user}',0,0)")
            connection.commit()

    #PUBLIC
    def get_name(self):
        return self.get('user')

    def get_score(self):
        return self.get('score')

    def get_money(self):
        return self.get('money')

    #PRIVATE
    def get(self, column):
        self.cursor.execute(f"SELECT {column} FROM members WHERE user = '{self.user}'")
        info = self.cursor.fetchone()
        return info[0]

    def exist(self):
        self.cursor.execute(f"SELECT user FROM members WHERE user = '{self.user}'")
        if (self.cursor.fetchone()):
            return True
        else:
            return False

class User(Penguin):
    def __init__(self, username, connection):
        super().__init__(username, connection)