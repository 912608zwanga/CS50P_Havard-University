import sys

def main():
    while True:
        print("\n Calculator\n")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Exit")

        choice = input("Select an option (1/2/3/4/5): ")

        if choice == "5":
            sys.exit("Thank You for using the Calculator")

        if choice in ["1", "2", "3", "4"]:
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"{n1} + {n2} = {add(n1, n2)}")
                elif choice == "2":
                    print(f"{n1} - {n2} = {subtract(n1, n2)}")
                elif choice == "3":
                    print(f"{n1} * {n2} = {multiply(n1, n2)}")
                elif choice == "4":
                    result = divide(n1, n2)
                    if result == "Error":
                        print("Division by zero not supported")
                    else:
                        print(f"{n1} / {n2} = {result}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        else:
            print("Invalid Option")

# These functions can now be tested because they don't use input()
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error"
    return n1 / n2

if __name__ == "__main__":
    main()
