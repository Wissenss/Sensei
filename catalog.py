from table import Table

class Catalog(Table):
    def __init__(self, name, connection):
        super().__init__(name, connection)
        self.default_parameters = ""

    def catalog_create(self):
        if not self.exist():
            self.create(self.default_parameters)
            

class CardCatalog(Catalog):
    def __init__(self, connection):
        name = 'CardCatalog'
        super().__init__(name, connection)
        self.default_parameters = """
                number INTEGER PRIMARY KEY,
                name TEXT,
                element TEXT,
                value INTEGER,
                color TEXT
                """
        self.file = 'Assets/load/cards.txt'

    def catalog_load(self):
        with open(self.file, 'r') as data:
            data = data.readlines()
            for entry in data:
                entry = entry.split('-')
                entry = "{}, '{}', '{}', {}, '{}'".format(entry[0], entry[1], entry[2], entry[3], entry[4]) 
                self.row_add(f"{entry}")