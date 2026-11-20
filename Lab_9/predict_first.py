from supplier import Supplier
from inventory import Inventory
from order import Order
from product_factory import ProductFactory
from discount_strategy import BulkDiscount, PercentageDiscount
from input_helpers import get_positive_float
from product_loader import load_products

supplier = Supplier("S001", "TechSupplies Ltd", "sales@techsupplies.com")

print("=== 2.3 Strategy: order of 250 ===")
lamp = ProductFactory.create("physical", "P001", "Desk Lamp", 25.00, 10,
                             supplier, weight=1.5)
order = Order("O001", BulkDiscount(200, 20))
order.add_order_line(lamp, 10)
print(f"BulkDiscount(200, 20): {order.calculate_total():.2f}")
order.set_discount(PercentageDiscount(10))
print(f"PercentageDiscount(10): {order.calculate_total():.2f}")

print("\n=== 2.4 Can two orders share one strategy? ===")
ten_percent = PercentageDiscount(10)
order_a = Order("A001", ten_percent)
order_b = Order("B001", ten_percent)
order_a.add_order_line(lamp, 2)
order_b.add_order_line(lamp, 4)
print(f"Order A total: {order_a.calculate_total():.2f}")
print(f"Order B total: {order_b.calculate_total():.2f}")

print("\n=== 5.2 Load products.csv ===")
load_products("products.csv", Inventory(), supplier)

print("\n=== 5.2 Load a missing file ===")
load_products("missing_products.csv", Inventory(), supplier)

print("\n=== 5.1 Enter abc, then -5, then 12.50 ===")
price = get_positive_float("Price: ")
print(f"Returned: {price}")

print("\n=== 3.2 Unknown product type (not caught) ===")
ProductFactory.create("service", "S001", "Installation", 30.00, 5, supplier)
print("This line never runs.")
