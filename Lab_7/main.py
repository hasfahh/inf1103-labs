import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory


def create_product_from_dict(item):
    product_type = item.get("type")

    if product_type == "physical":
        return PhysicalProduct(
            item["id"], item["name"], item["price"], item["stock"],
            item["weight"]
        )

    if product_type == "digital":
        return DigitalProduct(
            item["id"], item["name"], item["price"], item["stock"],
            item["download_size"]
        )

    print(f"Unknown product type for {item.get('id')}. Skipped.")
    return None


def load_inventory(inventory):
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            products = json.load(file)

        for item in products:
            product = create_product_from_dict(item)

            if product is not None:
                inventory.add_product(product)

        print("Inventory loaded successfully.")


def save_inventory(inventory):
    products = []

    for product in inventory.get_all_products():
        products.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

    print("Inventory saved successfully.")

def add_product_from_input(inventory):
    print("\nProduct Type")
    print("1. Physical Product")
    print("2. Digital Product")
    product_type = input("Choose type: ").strip()

    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    if product_type == "1":
        weight = float(input("Weight (kg): "))
        product = PhysicalProduct(product_id, name, price, stock, weight)
    else:
        download_size = float(input("Download Size (MB): "))
        product = DigitalProduct(product_id, name, price, stock, download_size)

    inventory.add_product(product)


def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")



inventory = Inventory()
load_inventory(inventory)

while True:
    display_menu()

    option = input("Enter option: ").strip()

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product_from_input(inventory)

    elif option == "3":
        product_id = input("Enter Product ID: ")
        quantity = int(input("New Stock Quantity: "))
        inventory.update_stock(product_id, quantity)

    elif option == "4":
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            product.display_information()
            print(f"    Fulfilment: {product.get_fulfilment_info()}")

            if isinstance(product, CanBeShipped):
                print(f"    Shipping Cost: ${product.calculate_shipping_cost():.2f}")
        else:
            print("Product not found.")

    elif option == "5":
        save_inventory(inventory)

    elif option == "6":
        save_inventory(inventory)
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")