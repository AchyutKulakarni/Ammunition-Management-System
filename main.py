from id_generator import unique_id_generator
from db_manager import DatabaseManager
from models import Ammunition
from inventory import Inventory
from data_generator import generate_ammo_batch
from utils import regex_search, sort_ammo, compare_ammunition
from import_export import import_from_csv, export_to_csv, export_to_json
from validation import validate_caliber, validate_manufacturer, validate_date

def main():
    # Initialize ID generator
    id_gen = unique_id_generator()


    # Setup database
    db = DatabaseManager()
    db.connect_db()
    db.create_tables()

    # Initialize inventory
    inventory = Inventory(db)

    # Generate bulk ammo data for testing
    bulk_ammos = generate_ammo_batch(5, id_gen)
    for ammo in bulk_ammos:
        inventory.add_ammunition(ammo)

    print("Initial Ammo Inventory:")
    inventory.list_all()

    # Example: Update quantity of first ammo
    first_ammo = bulk_ammos[0]
    inventory.update_ammunition_quantity(first_ammo.ammo_id, -20)  # Used 20 rounds
    print("\nAfter using 20 rounds of first ammo:")
    inventory.list_all()

    # Example: Regex search by caliber (e.g., search '9mm' partially)
    search_results = regex_search(inventory.ammo_list, 'caliber', '9', ignore_case=True)
    print("\nSearch Results for caliber matching '9':")
    for ammo in search_results:
        ammo.display_info()

    # Example: Sorting ammo by quantity descending
    sorted_ammos = sort_ammo(inventory.ammo_list, 'quantity', descending=True)
    print("\nAmmunition sorted by Quantity (desc):")
    for ammo in sorted_ammos:
        ammo.display_info()

    # Example: Export inventory data to CSV and JSON
    export_to_csv("ammo_export.csv", inventory.ammo_list)
    export_to_json("ammo_export.json", inventory.ammo_list)
    print("\nExported inventory to ammo_export.csv and ammo_export.json")

    # Example: Import ammo data from CSV (this CSV needs to exist with correct format)
    # imported_ammos = import_from_csv("ammo_import.csv", id_gen)
    # for ammo in imported_ammos:
    #     inventory.add_ammunition(ammo)

    # Example: Compare two ammo records from inventory
    if len(inventory.ammo_list) >= 2:
        diff = compare_ammunition(inventory.ammo_list[0], inventory.ammo_list[1])
        print("\nDifferences between first two ammo records:")
        print(diff)

    db.close()

if __name__ == "__main__":
    main()
