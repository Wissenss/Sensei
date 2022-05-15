import sqlite3

class Table:
    def __init__(self, name, connection):
        self.name = name
        self.connection = connection
        self.cursor = self.connection.cursor()

    def exist(self):
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE 'type=table' AND name = '{self.name}'")
        if self.cursor.fetchone():
            return True
        else:
            return False

    def create(self):
        self.cursor.execute(f"CREATE TABLE {self.name} (name TEXT);")
        self.connection.commit()

    def delete(self):
        if self.exist():
            self.cursor.execute("DROP TABLE ", self.name)
            self.connection.commit()

    def add_column(self, new_column, type = 'INTEGER'):
        if self.exist():
            self.cursor.execute("ALTER TABLE ", self.name, " ADD COLUMN ", new_column, type)
            self.connection.commit()

class Database:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.tables = []
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE 'type=table'")
        tables = self.cursor.fetchall()
        for table in tables:
            self.tables.append(Table(table, self.connection))
    
    def add_table(self, name):
        table = Table(name, self.connection).create()
        self.tables.append(table)

    def delete_table(self, name):
        table = Table(name, self.connection).delete()
        self.tables.remove(table)