import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Simplified Regex for Python: Just checks for #.#.#.# format
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        list_of_numbers = ip.split(".")

        for number in list_of_numbers:
            # Check for leading zeros: Catch "01" vs "1"
            if number != str(int(number)):
                return False

            # Check for range 0-255
            if int(number) < 0 or int(number) > 255:
                return False
        return True

    else:
        return False

if __name__ == "__main__":
    main()
