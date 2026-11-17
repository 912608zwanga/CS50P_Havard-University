# While forever
while True:
    # Get user input
    num = input("Fraction: ")
    index = num.find("/")

    try:
        # Try to split the fuel
        # Convert into integers
        x = int(num[:index])
        y = int(num[index + 1:])

        # Check if its less than 1 and stop the loop
        if x > y:
            continue

        # Calculate the percentage
        fraction = x / y
        break

    except (ValueError, ZeroDivisionError):
        continue

# Multiply percentage by 100
# Using round() is usually safer for fuel gauge problems
percentage = round(fraction * 100)

# Check if percentage is greater than 99, print F
if percentage >= 99:
    print("F")

# Check if percentage is less than 1, print E
elif percentage <= 1:
    print("E")

else:
    print(str(percentage) + "%")
