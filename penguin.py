import sqlite3

class Penguin:
    def __init__(self, username, connection):
        self.user = username
        self.connection = connection
        self.cursor = self.connection.cursor()
        if not self.exist():
            #add to members list
            self.cursor.execute(f"INSERT INTO members VALUES ('{self.user}',0,0)")
            connection.commit()

        self.cursor.execute(f"SELECT rowid FROM members WHERE user = '{self.user}'")
        self.id = self.cursor.fetchone()

        if not self.exist():
            #create inventories
            self.cursor.execute(f"CREATE TABLE cards_{self.id} (amount INTEGER);")
            connection.commit()

    ##PUBLIC##

    #get
    def get_name(self):
        return self.get('user')

    def get_score(self):
        return self.get('score')

    def get_money(self):
        return self.get('money')

    #inventory
    #card_inventory
    # def add_card(self, card_id):
    #     self.add_item(card_id, f'cards_{self.id}')
    
    # def remove_card(self, card_id):
    #     self.remove_item(card_id, f'cards_{self.id}')

    # def get_card(self, card_id):
    #     return self.get_item(card_id, 'cards_catalog')

    ##PRIVATE##
    # def get_item(self, item_id, inventory):
    #     self.cursor.execute(f"SELECT * FROM {inventory} WHERE rowid = {item_id}")
    #     return self.cursor.fetchone()

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