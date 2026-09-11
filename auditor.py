inventory = 0
failed_entries = 0


while True:
    stock_input = input("Enter stock quantity (or 'quit' to exit): ")

    # Check if user wants to quit
    if stock_input.lower() == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", failed_entries)
        break
