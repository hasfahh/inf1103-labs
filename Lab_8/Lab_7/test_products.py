from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped

print("=== Test 1: PhysicalProduct ===")
guitar = PhysicalProduct("P100", "Guitar", 350.00, 5, 4.5)
guitar.display_information()

print("\n=== Test 2: DigitalProduct ===")
windows = DigitalProduct("D100", "Operating System", 199.99, 100, 5200)
windows.display_information()

print("\n=== Test 3: get_fulfilment_info() ===")
print(guitar.get_fulfilment_info())
print(windows.get_fulfilment_info())

print("\n=== Test 4: Abstract Product cannot be instantiated ===")
try:
    product = Product("X001", "Generic", 10.00, 1)
    print("FAIL: Product was created")
except TypeError as error:
    print(f"PASS: {error}")

print("\n=== Test 5: Shipping cost for different weights ===")
for weight in [0.5, 2.0, 10.0]:
    item = PhysicalProduct("T", "Test Box", 1.00, 1, weight)
    print(f"{weight} kg -> ${item.calculate_shipping_cost():.2f}")

print("\n=== Test 6: Which products can be shipped? ===")
print(f"Guitar is CanBeShipped: {isinstance(guitar, CanBeShipped)}")
print(f"Operating System is CanBeShipped: {isinstance(windows, CanBeShipped)}")

print("\n=== Test 7: to_dict() keeps type and extra attribute ===")
print(guitar.to_dict())
print(windows.to_dict())