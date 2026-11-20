import unittest

from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory


class TestProductFactory(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "TechSupplies Ltd",
                                 "sales@techsupplies.com")

    def test_creates_physical_product(self):
        product = ProductFactory.create("physical", "P001", "Desk Lamp",
                                        25.00, 10, self.supplier, weight=1.5)
        self.assertIsInstance(product, PhysicalProduct)
        self.assertIsInstance(product, Product)

    def test_creates_digital_product(self):
        product = ProductFactory.create("digital", "D001", "Photo Editor",
                                        49.90, 100, self.supplier,
                                        download_size=850)
        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_type_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            ProductFactory.create("service", "S001", "Installation",
                                  30.00, 5, self.supplier)
        self.assertEqual(str(context.exception),
                         "Unknown product type: service")


if __name__ == "__main__":
    unittest.main()
