from table import Table

class Catalog(Table):
    def __init__(self, name, connection):
        super().__init__(name, connection)
        self.default_parameters = ""

    def catalog_create(self):
        if not self.exist():
            self.create(self.default_parameters)

    def load_file(self, file):
        with open(file, 'r') as data:
            data = data.readlines()
            for entry in data:
                entry = entry.split('-')
                print(entry)
                self.row_add(f"{entry}")


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

    def catalog_load(self):
        self.load_file('Assets/load/cards.txt')