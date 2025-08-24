import csv
import json
from models import Ammunition
from validation import validate_caliber, validate_date, validate_manufacturer

def import_from_csv(file_path, id_gen):
    ammos = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
           
            if not (validate_caliber(row['caliber']) and validate_manufacturer(row['manufacturer']) and
                    validate_date(row['date_manufactured']) and validate_date(row['expiry_date'])):
                continue  
                
            ammo_id = next(id_gen)
            ammo = Ammunition(
                ammo_id=ammo_id,
                caliber=row['caliber'],
                ammo_type=row['type'],
                quantity=int(row['quantity']),
                manufacturer=row['manufacturer'],
                price=float(row['price']),
                date_manufactured=row['date_manufactured'],
                expiry_date=row['expiry_date']
            )
            ammos.append(ammo)
    return ammos

def export_to_csv(file_path, ammo_list):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'caliber', 'ammo_type', 'quantity', 'manufacturer', 'price', 'date_manufactured', 'expiry_date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for ammo in ammo_list:
            writer.writerow({
                'id': ammo.ammo_id,
                'caliber': ammo.caliber,
                'ammo_type': ammo.ammo_type,
                'quantity': ammo.quantity,
                'manufacturer': ammo.manufacturer,
                'price': ammo.price,
                'date_manufactured': ammo.date_manufactured,
                'expiry_date': ammo.expiry_date,
            })

def export_to_json(file_path, ammo_list):
    with open(file_path, 'w') as jsonfile:
        json_list = [vars(ammo) for ammo in ammo_list]
        json.dump(json_list, jsonfile, indent=4)
