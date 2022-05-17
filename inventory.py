from table import Table
from catalog import CardCatalog, Catalog

class Inventory(Table):
    def __init__(self, name, connection):
        self.catalog = CardCatalog(connection)
        super().__init__(name, connection)
 
        default_parameters = """
                id INTEGER PRIMARY KEY,
                amount INTEGER
        """

        if (not self.exist()):
            self.create(default_parameters)

    def item_exist(self, item_id):
        return self.row_exist('id', item_id)

    def item_amount(self, item_id): #return the amount of an item on table self.name, column amount
        return self.row_get('id', item_id)[0][1]

    def item_add(self, item_id):
        if self.item_exist(item_id):
            self.cursor.execute(f"UPDATE {self.name} SET amount = amount + 1 WHERE id = '{item_id}'")
            self.connection.commit()
        else:
            default_values = f"'{item_id}', 1"
            self.row_add(default_values)

    def item_remove(self, item_id):
        amount = self.item_amount(item_id)
        if amount<1:
            return False

        if amount>1:
            self.cursor.execute(f"UPDATE {self.name} SET amount = amount - 1 WHERE id = '{item_id}'")
            self.connection.commit()
        else:
            self.row_delete('id', item_id)
        return True

    def item_get_attributes(self, item_id):
        return self.catalog.row_get('id', item_id)

class Deck(Inventory):
    def __init__(self, owner_id, connection):
        name = f"deck_{owner_id}"
        self.catalog = CardCatalog(connection)
        super().__init__(name, connection)