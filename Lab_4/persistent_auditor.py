# Initialize inventory and failed entries
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

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


# Main program loop
while True:
    stock = get_valid_input()

    # Check if user wants to quit
    if stock == "quit":
        break

    # Check if input was rejected
    if stock is None:
        failed_entries += 1
        continue

    # Process valid delivery
    inventory = process_delivery(inventory, stock)

    # Calculate tax for this delivery
    tax = calculate_tax(stock)

    print("Current Inventory:", inventory)
    print("Tax for this delivery:", tax)

    # Check for overstock
    if inventory > 500:
        print("ALERT: Inventory has exceeded maximum capacity of 500 units!")
        break
    elif inventory >= 400:
        print("WARNING: Inventory is nearing maximum capacity.")