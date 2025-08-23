import random
from models import Ammunition

caliber_list = ["9mm", ".45ACP", "5.56mm", "7.62mm", "12 Gauge", "22LR"]
ammo_types = ["Bullet", "Shell", "Cartridge"]
manufacturers = ["Acme Corp", "Best Ammo Inc", "Ammo Masters", "Secure Gun Supplies"]

def generate_ammo_batch(batch_size, id_gen):
    batch = []
    for _ in range(batch_size):
        ammo_id = next(id_gen)
        caliber = random.choice(caliber_list)
        ammo_type = random.choice(ammo_types)
        quantity = random.randint(50, 1000)
        manufacturer = random.choice(manufacturers)
        price = round(random.uniform(0.3, 2.5), 2)
        date_manufactured = "2023-01-01"
        expiry_date = "2028-01-01"
        ammo = Ammunition(ammo_id, caliber, ammo_type, quantity, manufacturer, price, date_manufactured, expiry_date)
        batch.append(ammo)
    return batch

