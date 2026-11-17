# Create menu dictionary
food_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Set total_amount to 0
total = 0.0

# Loop forever
while True:
    try:
        # Get user input and treat it case insensitively
        item = input("Item: ").title()

        # Check if item is in the dictionary (Ignore if it isn't)
        if item in food_menu:
            # Add the item price to total_amount
            total += food_menu[item]

            # Print the current total_amount with $ and 2 decimal places
            print(f"Total: ${total:.2f}")

    except EOFError:
        # Print a new line and stop the loop when Control-D is pressed
        print()
        break
