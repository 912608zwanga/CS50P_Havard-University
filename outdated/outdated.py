# Create list with the name of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Loop forever
while True:
    # Get user input
    date = input("Date: ").strip()

    try:
        # Split the date by /
        month, day, year = date.split("/")

        # Check if month is in between of 1 and 12 and day between 1 and 31
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            break

    except:
        try:
            # Split the date by space
            # Find the number of the month
            # Remove comma from day variable
            if "," in date:
                month_name, day_with_comma, year = date.split(" ")
                day = day_with_comma.replace(",", "")

                if month_name in months:
                    month = months.index(month_name) + 1

                    # Check if month is in between of 1 and 12 and day between 1 and 31
                    if 1 <= int(day) <= 31:
                        break
        except:
            # Go to the next line
            pass

# If month is less than 10, add a 0 before
# Using f-strings to handle the "add a 0 before" requirement for ISO 8601
print(f"{year}-{int(month):02}-{int(day):02}")
