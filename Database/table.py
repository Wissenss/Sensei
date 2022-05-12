import sqlite3

class Table:
    def __init__(self, limit, table, database = 'database.db'):
        self.limit = limit
        self.table = table
        self.database = database

    def connect(self):
        self.connection = sqlite3.connect(self.database)
        self.records = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def create_table(self):
        self.records.execute(f"SELECT * FROM {self.table}")
        check = self.records.fetchone()

        if not check:
            self.records

    def show_all(self):
        self.records.execute(f"SELECT rowid, * FROM {self.table}")
        items = self.records.fetchall()
        self.connection.commit

        for item in items:
            print(item)

Table(10, 'wololo')