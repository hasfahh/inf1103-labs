from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

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