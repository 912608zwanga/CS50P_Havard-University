import sys

def main():
    # Check the command line arguments
    check_command_line_arg()
    # Try to open the file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    # If can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Loop through the lines and check if starts with # or whitespace
    count = 0
    for line in lines:
        if not line.isspace() and not line.strip().startswith("#"):
            count += 1

    print(count)
    file.close()

# Function to check the command line arguments
def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if it is a Python file
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

def check_comment_or_empty_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()
