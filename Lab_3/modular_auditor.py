inventory = 0
failed_entries = 0


def get_valid_input():
    while True:
        stock_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

        if stock_input.lower() == "quit":
            return "quit"

        # Check for negative numbers
        if stock_input.startswith("-") and stock_input[1:].isdigit():
            print("Error: Stock quantity cannot be negative.")
            continue

        # Check for invalid input
        if not stock_input.isdigit():
            print("Error: Please enter a valid integer.")
            continue

        # Convert valid input to integer
        return int(stock_input)


value = get_valid_input()
print(value)