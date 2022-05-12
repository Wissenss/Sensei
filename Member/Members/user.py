from Database.table import Inventory

class User:
    def __init__(self, name, score, money):
        if not isinstance(name, str):
                raise TypeError("Invalid type...")
        self.name = name

        if not isinstance(score, int) or not isinstance(money, int):
            raise TypeError("Invalid type...")
        self.score = score
        self.money = money


"""
inventories = (items, puffles, iglues)

        for index in range(len(inventories)):
            if not isinstance(inventories[index], Inventory):
                raise TypeError("Invalid inventory...")
        self.items_inventory = items
        self.puffles_inventory = puffles
        self.iglues_inventory = iglues
"""
        