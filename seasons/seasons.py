import re
import sys
import inflect
from datetime import date

p = inflect.engine()

def main():
    # Get birth date from user
    birth_date = input("Date of Birth: ")

    try:
        # Validate and unpack the date
        year, month, day = check_birthday(birth_date)

        # Create date objects for math
        date_of_birth = date(int(year), int(month), int(day))
        date_of_today = date.today()

        # Calculate time difference
        diff = date_of_today - date_of_birth

        # Convert days into minutes (24 hours * 60 minutes)
        total_minutes = diff.days * 24 * 60

        # Convert the number to words without the word "and"
        output = p.number_to_words(total_minutes, andword="")

        # Capitalize the first word and add " minutes" at the end
        print(output.capitalize() + " minutes")

    except:
        # Exit if the date is invalid or format is wrong
        sys.exit("Invalid Date")


def check_birthday(birth_date):
    # Regex for YYYY-MM-DD format
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        # Split the string into year, month, and day
        year, month, day = birth_date.split("-")
        return year, month, day

    # Implicitly returns None if Regex fails, triggering the try/except
    return None


if __name__ == "__main__":
    main()
