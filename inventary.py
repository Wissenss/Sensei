import sqlite3  #database module

def add(user, item):
    connection = sqlite3.connect('database.db')
    records = connection.cursor()

    bag = f'inventory_{user}'

    try:
        records.execute(f"""CREATE TABLE {bag} (
            item_id INTEGER,
            amount INTEGER
        )""")
    except sqlite3.OperationalError: pass

    records.execute(f"SELECT item_id FROM {bag} WHERE item_id = {item}")
    check = records.fetchone()

    if(check):
        records.execute(f"""UPDATE {bag} SET amount = amount + 1
        WHERE item_id = {item}""")
    else:
        records.execute(f"INSERT INTO {bag} VALUES ('{item}','1')")

    connection.commit()
    connection.close()

def remove(user, item):
    connection = sqlite3.connect('database.db')
    records = connection.cursor()

    bag = f'inventory_{user}'

    try:
        records.execute(f"""CREATE TABLE {bag} (
            item_id INTEGER,
            amount INTEGER
        )""")
    except sqlite3.OperationalError: pass
    
    records.execute(f"SELECT amount FROM {bag} WHERE item_id = {item}")
    check = records.fetchone()

    if(check):
        if(check[0]<=1):
            records.execute(f"DELETE FROM {bag} WHERE item_id = {item}")
        else:
            records.execute(f"""UPDATE {bag} SET amount = amount - 1
            WHERE item_id = {item}""")
        connection.commit()
        connection.close()
        return True
    else:
        connection.close()
        return False