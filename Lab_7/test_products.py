from physical_product import PhysicalProduct
from digital_product import DigitalProduct

print("=== Test 1: PhysicalProduct ===")
guitar = PhysicalProduct("P100", "Guitar", 350.00, 5, 4.5)
guitar.display_information()

print("\n=== Test 2: DigitalProduct ===")
windows = DigitalProduct("D100", "Operating System", 199.99, 100, 5200)
windows.display_information()