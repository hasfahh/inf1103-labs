def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            return 0, []

        total = int(lines[0].strip())

        history = []

        if len(lines) > 1 and lines[1].strip():
            history = [int(value) for value in lines[1].strip().split(",")]

        return total, history

    except FileNotFoundError:
        return 0, []

def save_inventory(total, history):
    with open("inventory.txt", "w") as file:
        file.write(str(total) + "\n")
        file.write(",".join(str(value) for value in history))

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

inventory, transaction_history = load_inventory()
failed_entries = 0

while True:
    stock = get_valid_input()

    # Check if user wants to quit
    if stock == "quit":
        save_inventory(inventory, transaction_history)
        break

    # Check if input was rejected
    if stock is None:
        failed_entries += 1
        continue

    # Process valid delivery
    inventory = process_delivery(inventory, stock)

    transaction_history.append(stock)

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
