import sys
import csv
from tabulate import tabulate

def main():
    check_command_line_arg()

    # Create variable to store the table data
    table = []

    # Try to open the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)

    # If can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Print the table
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if it is a CSV file
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
