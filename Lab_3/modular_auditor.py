inventory = 0
failed_entries = 0


while True:
    stock_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

    # Check if user wants to quit
    if stock_input.lower() == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", failed_entries)
        break

    # Check for negative numbers
    if stock_input.startswith("-") and stock_input[1:].isdigit():
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue

    # Check for invalid input
    if not stock_input.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    # Convert valid input to integer
    stock = int(stock_input)

     # Add stock to inventory
    inventory += stock
    print("Current Inventory:", inventory)

    # Check for overstock
    if inventory > 500:
        print("ALERT: Inventory has exceeded maximum capacity of 500 units!")
        break
    elif inventory >= 400:
        print("WARNING: inventory is nearing maximum capacity:")

def get_valid_input():
    while True:
        user_input = input("Enter stock quantity or 'quit': ")

        if user_input.lower() == "quit":
            return "quit"

        try:
            quantity = int(user_input)

            if quantity < 0:
                print("Stock quantity cannot be negative.")
                continue

            return quantity

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
value = get_valid_input()
print(value)

