import sqlite3
from models import Ammunition

class DatabaseManager:
    def __init__(self, db_name="ammunition.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect_db(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Ammunition (
                                id TEXT PRIMARY KEY,
                                caliber TEXT NOT NULL,
                                type TEXT NOT NULL,
                                quantity INTEGER NOT NULL,
                                manufacturer TEXT,
                                price REAL,
                                date_manufactured TEXT,
                                expiry_date TEXT
                              )''')
        self.conn.commit()

    def insert_ammunition(self, ammo):
        self.cursor.execute('''INSERT OR IGNORE INTO Ammunition (id, caliber, type, quantity, manufacturer, price, date_manufactured, expiry_date)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                            (ammo.ammo_id, ammo.caliber, ammo.ammo_type, ammo.quantity,
                             ammo.manufacturer, ammo.price, ammo.date_manufactured, ammo.expiry_date))
        self.conn.commit()

    def update_quantity(self, ammo_id, new_quantity):
        self.cursor.execute('UPDATE Ammunition SET quantity = ? WHERE id = ?', (new_quantity, ammo_id))
        self.conn.commit()

    def update_ammunition(self, ammo):
        self.cursor.execute('''UPDATE Ammunition SET caliber = ?, type = ?, quantity = ?, manufacturer = ?, price = ?, date_manufactured = ?, expiry_date = ?
                               WHERE id = ?''',
                            (ammo.caliber, ammo.ammo_type, ammo.quantity, ammo.manufacturer, ammo.price, ammo.date_manufactured, ammo.expiry_date, ammo.ammo_id))
        self.conn.commit()

    def delete_ammunition(self, ammo_id):
        self.cursor.execute('DELETE FROM Ammunition WHERE id = ?', (ammo_id,))
        self.conn.commit()

    def fetch_all_ammunition(self):
        self.cursor.execute('SELECT * FROM Ammunition')
        rows = self.cursor.fetchall()
        ammos = []
        for row in rows:
            ammo = Ammunition(*row)
            ammos.append(ammo)
        return ammos

    def fetch_ammunition_by_id(self, ammo_id):
        self.cursor.execute('SELECT * FROM Ammunition WHERE id = ?', (ammo_id,))
        row = self.cursor.fetchone()
        if row:
            return Ammunition(*row)
        return None

    def close(self):
        if self.conn:
            self.conn.close()

