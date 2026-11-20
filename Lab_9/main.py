import json

from supplier import Supplier
from product import Product
from product_factory import ProductFactory
from can_be_shipped import CanBeShipped
from inventory import Inventory
from order import Order
from discount_strategy import (DiscountStrategy, NoDiscount,
                               PercentageDiscount, BulkDiscount,
                               StudentDiscount)
from input_helpers import (get_positive_float, get_non_negative_int,
                           get_positive_int)



def get_or_create_supplier(suppliers: dict[str, Supplier], supplier_id: str,
                           name: str, contact_email: str) -> Supplier:
    if supplier_id not in suppliers:
        suppliers[supplier_id] = Supplier(supplier_id, name, contact_email)

    return suppliers[supplier_id]


def create_product_from_dict(item: dict,
                             suppliers: dict[str, Supplier]) -> Product:
    supplier_data = item["supplier"]
    supplier = get_or_create_supplier(
        suppliers, supplier_data["id"], supplier_data["name"],
        supplier_data["email"]
    )

    return ProductFactory.create(
        item["type"], item["id"], item["name"], item["price"], item["stock"],
        supplier,
        weight=item.get("weight", 0.0),
        download_size=item.get("download_size", 0.0)
    )


def load_inventory(inventory: Inventory,
                   suppliers: dict[str, Supplier]) -> None:
    try:
        with open("inventory.json", "r") as file:
            products = json.load(file)
    except FileNotFoundError:
        print("No saved inventory found. Starting with an empty inventory.")
        return
    except json.JSONDecodeError:
        print("inventory.json is damaged. Starting with an empty inventory.")
        return

    for item in products:
        try:
            product = create_product_from_dict(item, suppliers)
        except (ValueError, KeyError) as error:
            print(f"Skipped invalid product {item.get('id')}: {error}")
        else:
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
    choice = input("Choose type: ").strip()

    if choice not in ("1", "2"):
        print("Invalid product type.")
        return

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = get_positive_float("Price: ")
    stock = get_non_negative_int("Stock Quantity: ")
    supplier = select_supplier(suppliers)

    if choice == "1":
        weight = get_positive_float("Weight (kg): ")
        product = ProductFactory.create("physical", product_id, name, price,
                                        stock, supplier, weight=weight)
    else:
        download_size = get_positive_float("Download Size (MB): ")
        product = ProductFactory.create("digital", product_id, name, price,
                                        stock, supplier,
                                        download_size=download_size)

    inventory.add_product(product)


def choose_discount() -> DiscountStrategy:
    print("\nDiscount")
    print("1. No Discount")
    print("2. 10% Off")
    print("3. $20 Off Orders of $200 or More")
    print("4. Student Discount (5%)")
    choice = input("Choose discount: ").strip()

    if choice == "2":
        return PercentageDiscount(10)
    if choice == "3":
        return BulkDiscount(200, 20)
    if choice == "4":
        return StudentDiscount()

    return NoDiscount()


def create_order(inventory: Inventory) -> None:
    order_id = input("Order ID: ")
    order = Order(order_id, choose_discount())

    while True:
        product_id = input("Product ID to add (blank to finish): ").strip()

        if product_id == "":
            break

        product = inventory.find_product(product_id)

        if product is None:
            print("Product not found.")
            continue

        quantity = get_positive_int("Quantity: ")
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