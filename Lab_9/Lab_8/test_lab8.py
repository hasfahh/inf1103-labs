from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_association() -> None:
    print("\n=== Section 2: Association (Supplier - Product) ===")
    supplier = Supplier("S001", "TechSupplies Ltd", "sales@techsupplies.com")
    laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.2)
    antivirus = DigitalProduct("D001", "Antivirus Licence", 59.99, 100,
                               supplier, 350)

    print(f"Same supplier object? {laptop.get_supplier() is antivirus.get_supplier()}")

    del supplier
    print("After 'del supplier':")
    laptop.get_supplier().display_information()
    antivirus.get_supplier().display_information()


def test_aggregation() -> None:
    print("\n=== Section 3: Aggregation (Inventory - Product) ===")
    supplier = Supplier("S002", "Office World", "orders@officeworld.com")
    mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, supplier, 0.1)

    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(mouse)
    inventory_a.remove_product("P002")

    print(f"Still in Inventory A? {inventory_a.find_product('P002') is not None}")
    print("Product still works after removal:")
    mouse.display_information()

    inventory_b.add_product(mouse)
    print(f"Same object in Inventory B? {inventory_b.find_product('P002') is mouse}")


def test_composition() -> None:
    print("\n=== Section 4: Composition (Order - OrderLine) ===")
    supplier = Supplier("S001", "TechSupplies Ltd", "sales@techsupplies.com")
    laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.2)
    antivirus = DigitalProduct("D001", "Antivirus Licence", 59.99, 100,
                               supplier, 350)

    order_1 = Order("O001")
    order_1.add_order_line(laptop, 2)
    order_1.add_order_line(antivirus, 3)
    order_1.display_order()

    order_2 = Order("O002")
    order_2.add_order_line(laptop, 1)
    order_2.display_order()

    line_1 = order_1.get_order_lines()[0]
    line_2 = order_2.get_order_lines()[0]
    print(f"Same OrderLine object? {line_1 is line_2}")
    print(f"Same Product object?   {line_1.get_product() is line_2.get_product()}")
    print(f"OrderLine ids: {id(line_1)} vs {id(line_2)}")

    order_1.remove_order_line("D001")
    order_1.display_order()


def test_lsp_and_polymorphism() -> None:
    print("\n=== Sections 6 & 7: LSP and Polymorphism ===")
    supplier = Supplier("S003", "Soft Inc", "hello@softinc.com")
    keyboard = PhysicalProduct("P003", "Keyboard", 45.00, 25, supplier, 0.8)
    editor = DigitalProduct("D002", "Photo Editor", 89.99, 50, supplier, 1200)

    print("-- show_product_details() with each subclass --")
    show_product_details(keyboard)
    show_product_details(editor)

    print("-- update_stock() behaves the same for both --")
    keyboard.update_stock(30)
    editor.update_stock(60)

    print("-- One loop over the Product collection --")
    inventory = Inventory()
    inventory.add_product(keyboard)
    inventory.add_product(editor)

    for product in inventory.get_all_products():
        product.display_information()
        print(product.get_fulfilment_info())


test_association()
test_aggregation()
test_composition()
test_lsp_and_polymorphism()