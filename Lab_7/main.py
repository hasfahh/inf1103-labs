import json
import os

from product import Product
from inventory import Inventory


def load_inventory(inventory):
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            products = json.load(file)

        for item in products:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            inventory.add_product(product)

        print("Inventory loaded successfully.")


def save_inventory(inventory):
    products = []

    for product in inventory.get_all_products():
        products.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

    print("Inventory saved successfully.")


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
        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        product = Product(product_id, name, price, stock)
        inventory.add_product(product)

    elif option == "3":
        product_id = input("Enter Product ID: ")
        quantity = int(input("New Stock Quantity: "))
        inventory.update_stock(product_id, quantity)

    elif option == "4":
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            product.display_information()
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