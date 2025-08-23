class Inventory:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.ammo_list = self.db_manager.fetch_all_ammunition()

    def add_ammunition(self, ammo):
        self.db_manager.insert_ammunition(ammo)
        self.ammo_list.append(ammo)

    def remove_ammunition(self, ammo_id):
        self.db_manager.delete_ammunition(ammo_id)
        self.ammo_list = [ammo for ammo in self.ammo_list if ammo.ammo_id != ammo_id]

    def update_ammunition_quantity(self, ammo_id, amount):
        for ammo in self.ammo_list:
            if ammo.ammo_id == ammo_id:
                ammo.update_quantity(amount)
                self.db_manager.update_quantity(ammo_id, ammo.quantity)
                break

    def update_ammunition(self, ammo):
        for idx, a in enumerate(self.ammo_list):
            if a.ammo_id == ammo.ammo_id:
                self.ammo_list[idx] = ammo
                self.db_manager.update_ammunition(ammo)
                break

    def list_all(self):
        for ammo in self.ammo_list:
            ammo.display_info()

    def find_ammunition_by_id(self, ammo_id):
        for ammo in self.ammo_list:
            if ammo.ammo_id == ammo_id:
                return ammo
        return None

