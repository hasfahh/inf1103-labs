import json
import os

from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from order import Order


def get_or_create_supplier(suppliers: dict[str, Supplier], supplier_id: str,
                           name: str, contact_email: str) -> Supplier:
    if supplier_id not in suppliers:
        suppliers[supplier_id] = Supplier(supplier_id, name, contact_email)

    return suppliers[supplier_id]


def create_product_from_dict(item: dict,
                             suppliers: dict[str, Supplier]) -> Product | None:
    supplier_data = item["supplier"]
    supplier = get_or_create_supplier(
        suppliers, supplier_data["id"], supplier_data["name"],
        supplier_data["email"]
    )

    product_type = item.get("type")

    if product_type == "physical":
        return PhysicalProduct(
            item["id"], item["name"], item["price"], item["stock"],
            supplier, item["weight"]
        )

    if product_type == "digital":
        return DigitalProduct(
            item["id"], item["name"], item["price"], item["stock"],
            supplier, item["download_size"]
        )

    print(f"Unknown product type for {item.get('id')}. Skipped.")
    return None


def load_inventory(inventory: Inventory,
                   suppliers: dict[str, Supplier]) -> None:
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            products = json.load(file)

        for item in products:
            product = create_product_from_dict(item, suppliers)

            if product is not None:
                inventory.add_product(product)

        print("Inventory loaded successfully.")


def save_inventory(inventory: Inventory) -> None:
    products = []

    for product in inventory.get_all_products():
        products.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

    print("Inventory saved successfully.")


def select_supplier(suppliers: dict[str, Supplier]) -> Supplier:
    supplier_id = input("Supplier ID: ")

    if supplier_id in suppliers:
        print(f"Using existing supplier: {suppliers[supplier_id].get_name()}")
        return suppliers[supplier_id]

    name = input("Supplier Name: ")
    contact_email = input("Supplier Email: ")
    return get_or_create_supplier(suppliers, supplier_id, name, contact_email)


def add_product_from_input(inventory: Inventory,
                           suppliers: dict[str, Supplier]) -> None:
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
    supplier = select_supplier(suppliers)

    product: Product

    if product_type == "1":
        weight = float(input("Weight (kg): "))
        product = PhysicalProduct(product_id, name, price, stock,
                                  supplier, weight)
    else:
        download_size = float(input("Download Size (MB): "))
        product = DigitalProduct(product_id, name, price, stock,
                                 supplier, download_size)

    inventory.add_product(product)


def create_order(inventory: Inventory) -> None:
    order_id = input("Order ID: ")
    order = Order(order_id)

    while True:
        product_id = input("Product ID to add (blank to finish): ").strip()

        if product_id == "":
            break

        product = inventory.find_product(product_id)

        if product is None:
            print("Product not found.")
            continue

        quantity = int(input("Quantity: "))
        order.add_order_line(product, quantity)

    order.display_order()


def display_menu() -> None:
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Remove Product")
    print("6. Create Order")
    print("7. Save Inventory")
    print("8. Exit")
    print("----------------------------")


suppliers: dict[str, Supplier] = {}
inventory = Inventory()
load_inventory(inventory, suppliers)

while True:
    display_menu()

    option = input("Enter option: ").strip()

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product_from_input(inventory, suppliers)

    elif option == "3":
        product_id = input("Enter Product ID: ")
        quantity = int(input("New Stock Quantity: "))
        inventory.update_stock(product_id, quantity)

    elif option == "4":
        product_id = input("Enter Product ID: ")
        product = inventory.find_product(product_id)

        if product is not None:
            product.display_information()
            print(f"    Fulfilment: {product.get_fulfilment_info()}")

            if isinstance(product, CanBeShipped):
                print(f"    Shipping Cost: ${product.calculate_shipping_cost():.2f}")
        else:
            print("Product not found.")

    elif option == "5":
        product_id = input("Enter Product ID: ")
        inventory.remove_product(product_id)

    elif option == "6":
        create_order(inventory)

    elif option == "7":
        save_inventory(inventory)

    elif option == "8":
        save_inventory(inventory)
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")