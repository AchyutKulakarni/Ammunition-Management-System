import datetime

class Ammunition:
    def __init__(self, ammo_id, caliber, ammo_type, quantity, manufacturer, price, date_manufactured, expiry_date):
        self.ammo_id = ammo_id
        self.caliber = caliber
        self.ammo_type = ammo_type
        self.quantity = quantity
        self.manufacturer = manufacturer
        self.price = price
        self.date_manufactured = date_manufactured
        self.expiry_date = expiry_date

    def display_info(self):
        info = (f"ID: {self.ammo_id}, Caliber: {self.caliber}, Type: {self.ammo_type}, Quantity: {self.quantity}, "
                f"Manufacturer: {self.manufacturer}, Price: {self.price}, Manufactured On: {self.date_manufactured}, "
                f"Expires On: {self.expiry_date}")
        print(info)

    def update_quantity(self, amount):
        self.quantity += amount

    def is_expired(self):
        return datetime.datetime.strptime(self.expiry_date, "%Y-%m-%d").date() < datetime.date.today()

