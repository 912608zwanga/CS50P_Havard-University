# Create empty dictionary
grocery_list = {}

# Loop forever
while True:
    try:
        # Get user input and treat it case-insensitively by converting to upper right away
        item = input().strip().upper()

        # Check if item is already in the dictionary
        if item in grocery_list:
            # If it is, add 1 to the count
            grocery_list[item] += 1
        else:
            # Otherwise, add the item for the first time
            grocery_list[item] = 1

    except EOFError:
        # Print a new line for a clean exit
        print()

        # Print all the items in alphabetical order
        # sorted() on a dictionary returns a sorted list of its keys
        for item in sorted(grocery_list.keys()):
            # Prefix each line with the number of times the item was inputted
            print(f"{grocery_list[item]} {item}")

        # Stop the while loop
        break
