"""
# Get user inputs
expression = input("Expression: ")
x, y, z = expression.split(" ")

# Convert variables into float

x_value = float(x)
z_value = float(z)

if y == "+":
    result = (x_value + z_value)
elif y == "-":
    result = (x_value - z_value)
elif y == "*":
    result = (x_value * z_value)
elif y == "/":
    result = (x_value / z_value)
else:
    result = "Invalid operator"

print(round(result, 1))
"""
# Get user inputs
try:
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x_value = float(x)
    z_value = float(z)

    if y == "+":
        result = x_value + z_value
    elif y == "-":
        result = x_value - z_value
    elif y == "*":
        result = x_value * z_value
    elif y == "/":
        if z_value == 0:
            print("Error: Division by zero.")
            exit(1)
        result = x_value / z_value
    else:
        print("Invalid operator")
        exit(1)

    print(round(result, 1))
except ValueError:
    print("Invalid input format. Please enter: number operator number")
except Exception as e:
    print(f"Error: {e}")
