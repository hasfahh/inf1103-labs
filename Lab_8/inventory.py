from product import Product


class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        print("Product added successfully!")

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product is not None:
            self.__products.remove(product)
            print("Product removed from inventory.")
        else:
            print("Product not found.")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("------------------------------------------------")

        if not self.__products:
            print("No products available.")

        for product in self.__products:
            product.display_information()

        print("------------------------------------------------")

    def update_stock(self, product_id: str, quantity: int) -> None:
        product = self.find_product(product_id)

        if product is not None:
            product.update_stock(quantity)
        else:
            print("Product not found.")

    def get_all_products(self) -> list[Product]:
        return self.__products