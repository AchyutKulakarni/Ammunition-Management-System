# from id_generator import unique_id_generator
# from db_manager import DatabaseManager
# from models import Ammunition
# from inventory import Inventory
# from data_generator import generate_ammo_batch
# from utils import regex_search, sort_ammo, compare_ammunition
# from import_export import import_from_csv, export_to_csv, export_to_json
# from validation import validate_caliber, validate_manufacturer, validate_date

# def main():
#     # Initialize ID generator
#     id_gen = unique_id_generator()


#     # Setup database
#     db = DatabaseManager()
#     db.connect_db()
#     db.create_tables()

#     # Initialize inventory
#     inventory = Inventory(db)

#     # Generate bulk ammo data for testing
#     bulk_ammos = generate_ammo_batch(5, id_gen)
#     for ammo in bulk_ammos:
#         inventory.add_ammunition(ammo)

#     print("Initial Ammo Inventory:")
#     inventory.list_all()

#     # Example: Update quantity of first ammo
#     first_ammo = bulk_ammos[0]
#     inventory.update_ammunition_quantity(first_ammo.ammo_id, -20)  # Used 20 rounds
#     print("\nAfter using 20 rounds of first ammo:")
#     inventory.list_all()

#     # Example: Regex search by caliber (e.g., search '9mm' partially)
#     search_results = regex_search(inventory.ammo_list, 'caliber', '9', ignore_case=True)
#     print("\nSearch Results for caliber matching '9':")
#     for ammo in search_results:
#         ammo.display_info()

#     # Example: Sorting ammo by quantity descending
#     sorted_ammos = sort_ammo(inventory.ammo_list, 'quantity', descending=True)
#     print("\nAmmunition sorted by Quantity (desc):")
#     for ammo in sorted_ammos:
#         ammo.display_info()

#     # Example: Export inventory data to CSV and JSON
#     export_to_csv("ammo_export.csv", inventory.ammo_list)
#     export_to_json("ammo_export.json", inventory.ammo_list)
#     print("\nExported inventory to ammo_export.csv and ammo_export.json")

#     # Example: Import ammo data from CSV (this CSV needs to exist with correct format)
#     # imported_ammos = import_from_csv("ammo_import.csv", id_gen)
#     # for ammo in imported_ammos:
#     #     inventory.add_ammunition(ammo)

#     # Example: Compare two ammo records from inventory
#     if len(inventory.ammo_list) >= 2:
#         diff = compare_ammunition(inventory.ammo_list[0], inventory.ammo_list[1])
#         print("\nDifferences between first two ammo records:")
#         print(diff)

#     db.close()

# if __name__ == "__main__":
#     main()


from id_generator import unique_id_generator
from db_manager import DatabaseManager
from models import Ammunition
from inventory import Inventory
from data_generator import generate_ammo_batch
from utils import regex_search, sort_ammo, compare_ammunition
from import_export import import_from_csv, export_to_csv, export_to_json
from validation import validate_caliber, validate_manufacturer, validate_date

def print_menu():
    print("\nAmmunition Management System")
    print("1. Show all ammunition")
    print("2. Add sample batch of ammunition")
    print("3. Update quantity of an ammunition by ID")
    print("4. Search ammunition by regex pattern")
    print("5. Sort inventory by field")
    print("6. Export inventory to CSV and JSON")
    print("7. Compare two ammunition records by ID")
    print("8. Clear database")
    print("9. Exit")

def main():
    id_gen = unique_id_generator(start=1000)
    db = DatabaseManager()
    db.connect_db()
    db.create_tables()
    inventory = Inventory(db)

    while True:
        print_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == '1':
            print("\nCurrent Inventory:")
            inventory.list_all()

        elif choice == '2':
            try:
                count = int(input("Enter how many sample records to add: "))
                batch = generate_ammo_batch(count, id_gen)
                for ammo in batch:
                    inventory.add_ammunition(ammo)
                inventory.ammo_list = db.fetch_all_ammunition()
                print(f"{count} sample ammunition records added.")
            except ValueError:
                print("Invalid number.")

        elif choice == '3':
            ammo_id = input("Enter ammunition ID to update quantity: ").strip()
            ammo = inventory.find_ammunition_by_id(ammo_id)
            if ammo:
                try:
                    amount = int(input(f"Enter quantity change (positive to add, negative to use): "))
                    inventory.update_ammunition_quantity(ammo_id, amount)
                    print(f"Quantity updated. New quantity: {ammo.quantity}")
                except ValueError:
                    print("Invalid quantity.")
            else:
                print("Ammunition ID not found.")

        elif choice == '4':
            field = input("Enter field to search by (caliber/ammo_type/manufacturer): ").strip()
            pattern = input("Enter regex pattern to search: ").strip()
            results = regex_search(inventory.ammo_list, field, pattern)
            print(f"\nSearch results for pattern '{pattern}' in {field}:")
            if results:
                for r in results:
                    r.display_info()
            else:
                print("No matches found.")

        elif choice == '5':
            field = input("Enter field to sort by (caliber/type/quantity/manufacturer/price): ").strip()
            order = input("Sort descending? (y/n): ").strip().lower()
            descending = order == 'y'
            sorted_list = sort_ammo(inventory.ammo_list, field, descending)
            print(f"\nInventory sorted by {field} {'descending' if descending else 'ascending'}:")
            for ammo in sorted_list:
                ammo.display_info()

        elif choice == '6':
            csv_path = input("Enter filename to export CSV (e.g. inventory.csv): ").strip()
            json_path = input("Enter filename to export JSON (e.g. inventory.json): ").strip()
            export_to_csv(csv_path, inventory.ammo_list)
            export_to_json(json_path, inventory.ammo_list)
            print(f"Exported inventory to {csv_path} and {json_path}")

        elif choice == '7':
            id1 = input("Enter first ammunition ID to compare: ").strip()
            id2 = input("Enter second ammunition ID to compare: ").strip()
            ammo1 = inventory.find_ammunition_by_id(id1)
            ammo2 = inventory.find_ammunition_by_id(id2)
            if ammo1 and ammo2:
                diffs = compare_ammunition(ammo1, ammo2)
                if diffs:
                    print("\nDifferences:")
                    for field, change in diffs.items():
                        print(f"- {field}: {change['old']} -> {change['new']}")
                else:
                    print("Records are identical.")
            else:
                print("One or both ammunition IDs not found.")

        elif choice == '8':
            db.clear_database()
            inventory.ammo_list.clear()  
            print("Database cleared.")

        elif choice == '9':
            print("Exiting...")
            db.close()
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
