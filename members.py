from table import Table
from inventory import Deck

class Members(Table):
    def __init__(self, connection):
        name = 'members'
        self.username = ''
        super().__init__(name, connection)

    def members_create(self):
        default_parameters = """
                user TEXT,
                score INTEGER,
                money INTEGER
        """
        if not self.exist():
            self.create(default_parameters)

    def member_exist(self):
        return self.row_exist('user', self.username)

    def member_add(self):
        default_values = f"'{self.username}', 0, 0"
        self.row_add(default_values)

    def member_get(self):
        return self.row_get('user', self.username)

class Penguin(Members):
    def __init__(self, discord_id, connection):
        super().__init__(connection)
        self.username = discord_id

        if not self.member_exist():
            self.member_add()

        row = self.member_get()
        self.id = row[0][0]
        self.score = row[0][2]
        self.money = row[0][3]

        #inventories
        self.deck_inventory = Deck(self.id, self.connection)

class User(Penguin):
    def __init__(self, username, connection):
        super().__init__(username, connection)