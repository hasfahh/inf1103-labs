import csv

from supplier import Supplier
from inventory import Inventory
from product_factory import ProductFactory


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0

        with file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                try:
                    product = ProductFactory.create(
                        row[0], row[1], row[2], float(row[3]), int(row[4]),
                        supplier
                    )
                except ValueError as error:
                    print(f"Skipped row {row}: {error}")
                else:
                    inventory.add_product(product)
                    loaded += 1

        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")