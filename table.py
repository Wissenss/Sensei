import sqlite3

class Table:
    def __init__(self, name, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.name = name

    def exist(self):
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name ='{self.name}'")
        check = self.cursor.fetchone()
        if check:
            return True
        else:
            return False

    def row_exist(self, column, check):
        self.cursor.execute(f"SELECT * FROM {self.name} WHERE {column} = '{check}'")
        if self.cursor.fetchone():
            return True
        else:
            return False

    def row_add(self, values):
        self.cursor.execute(f"INSERT INTO {self.name} VALUES ({values})")
        self.connection.commit()

    def row_delete(self, column, check):
        self.cursor.execute(f"DELETE FROM {self.name} WHERE {column} = {check}")
        self.connection.commit()

    def row_get(self, column, check):
        self.cursor.execute(f"SELECT rowid, * FROM {self.name} WHERE {column} = '{check}'")
        return self.cursor.fetchall()

    def create(self, parameters):
        self.cursor.execute(f"CREATE TABLE {self.name} ({parameters});")
        self.connection.commit()

    def delete(self):
        self.cursor.execute(f"DROP TABLE {self.name}")
        self.connection.commit()