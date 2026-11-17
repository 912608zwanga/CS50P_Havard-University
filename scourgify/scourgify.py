import sys
import csv

def main():
    # Check command line argumments
    check_command_line_arg()

    # Try to open the file
    try:
        with open(sys.argv[1], "r") as input_file:
            reader = csv.DictReader(input_file)
            new_data = []

            for row in reader:
                # Create name, last name
                last, first = row["name"].split(", ")

                # Add them to dict
                new_data.append({"first": first, "last": last, "house": row["house"]})

    # If can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Write new csv file
    with open(sys.argv[2], "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in new_data:
            writer.writerow(row)


def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if it is a CSV file
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
