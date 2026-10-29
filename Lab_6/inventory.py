from product import Product


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)
        print("Product added successfully!")

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")

        if not self.__products:
            print("No products available.")

        for product in self.__products:
            product.display_information()

        print("------------------------------------------------")


    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def update_stock(self, product_id, quantity):
        product = self.search_product(product_id)

        if product is not None:
            product.update_stock(quantity)
        else:
            print("Product not found.")

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    def get_all_products(self):
        return self.__products