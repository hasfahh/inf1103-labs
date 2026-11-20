import unittest

from supplier import Supplier
from product_factory import ProductFactory
from order_line import OrderLine


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "TechSupplies Ltd",
                                 "sales@techsupplies.com")
        self.product = ProductFactory.create("physical", "P001", "Desk Lamp",
                                             25.00, 10, self.supplier,
                                             weight=1.5)

    def test_price_must_be_greater_than_zero(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P002", "Free Lamp", 0, 10,
                                  self.supplier)

    def test_stock_cannot_be_negative_on_creation(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D002", "Bad Stock", 9.99, -1,
                                  self.supplier)

    def test_stock_cannot_be_updated_to_negative(self):
        with self.assertRaises(ValueError):
            self.product.update_stock(-5)

    def test_order_line_quantity_must_be_greater_than_zero(self):
        with self.assertRaises(ValueError):
            OrderLine(self.product, 0)


if __name__ == "__main__":
    unittest.main()
