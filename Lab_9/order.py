from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy, NoDiscount


class Order:
    def __init__(self, order_id: str,
                 discount: DiscountStrategy | None = None) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

        if discount is None:
            discount = NoDiscount()

        self.__discount: DiscountStrategy = discount

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                print("Order line removed.")
                return

        print("Order line not found.")

    def calculate_subtotal(self) -> float:
        return sum(line.calculate_subtotal() for line in self.__order_lines)

    def calculate_total(self) -> float:
        return self.__discount.apply(self.calculate_subtotal())

    def display_order(self) -> None:
        print(f"\nOrder {self.__order_id}")
        print("------------------------------------------------")

        if not self.__order_lines:
            print("No order lines.")

        for order_line in self.__order_lines:
            order_line.display_information()

        print("------------------------------------------------")
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
        print(f"Total after discount: ${self.calculate_total():.2f}")

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)
