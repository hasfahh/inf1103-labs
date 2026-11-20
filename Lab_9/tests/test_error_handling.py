import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from supplier import Supplier
from inventory import Inventory
from input_helpers import get_positive_float
from product_loader import load_products

CSV_CONTENT = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


class TestUserInput(unittest.TestCase):
    @patch("builtins.input", side_effect=["abc", "-5", "12.50"])
    def test_keeps_asking_until_valid(self, mock_input):
        output = io.StringIO()

        with redirect_stdout(output):
            value = get_positive_float("Price: ")

        self.assertEqual(value, 12.50)
        self.assertIn("Please enter a valid number", output.getvalue())
        self.assertIn("Please enter a number greater than zero.",
                      output.getvalue())


class TestLoadProducts(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "TechSupplies Ltd",
                                 "sales@techsupplies.com")
        self.inventory = Inventory()

    def test_valid_rows_load_and_bad_rows_are_skipped(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "products.csv")

            with open(path, "w", newline="") as file:
                file.write(CSV_CONTENT)

            output = io.StringIO()
            with redirect_stdout(output):
                load_products(path, self.inventory, self.supplier)

        self.assertEqual(len(self.inventory.get_all_products()), 3)
        self.assertIn("Unknown product type: service", output.getvalue())
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())

    def test_missing_file_is_handled(self):
        output = io.StringIO()

        with redirect_stdout(output):
            load_products("missing.csv", self.inventory, self.supplier)

        self.assertEqual(len(self.inventory.get_all_products()), 0)
        self.assertIn("Products file not found", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
