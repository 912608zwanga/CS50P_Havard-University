def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # vanity plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable ... vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a '0'

    number_found = False

    for i in range(len(s)):
        # Check for invalid characters (periods, spaces, or punctuations marks)
        if not s[i].isalnum():
            return False

        if s[i].isdigit():
            # Check Rule: The first number used cannot be a '0'
            if not number_found and s[i] == '0':
                return False
            number_found = True

        # Check Rule: Numbers cannot be used in the middle of a plate (letter after a number)
        elif number_found and s[i].isalpha():
            return False

    # if we pass all the tests, return True
    return True

if __name__ == "__main__":
    main()
