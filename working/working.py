import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(s):
    # 9 AM to 5 PM      -->  09:00 to 17:00
    # 9:00 AM to 5:00 PM  -->  09:00 to 17:00
    # 10:30 PM to 8:50 AM  -->  22:30 to 08:50
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)

    if time:
        # Check if hour values are valid (1-12)
        if int(time.group(1)) > 12 or int(time.group(4)) > 12:
            raise ValueError

        # Check if minute values are valid (< 60)
        if time.group(2):
            if int(time.group(2)) >= 60:
                raise ValueError
        if time.group(5):
            if int(time.group(5)) >= 60:
                raise ValueError

        # time1
        hour1 = int(time.group(1))
        if time.group(3).upper() == "PM":
            if hour1 != 12:
                hour1 += 12
        elif time.group(3).upper() == "AM" and hour1 == 12:
            hour1 = 0

        if time.group(2) == None:
            time1 = f"{hour1:02}:00"
        else:
            time1 = f"{hour1:02}:{time.group(2)}"

        # time2
        hour2 = int(time.group(4))
        if time.group(6).upper() == "PM":
            if hour2 != 12:
                hour2 += 12
        elif time.group(6).upper() == "AM" and hour2 == 12:
            hour2 = 0

        if time.group(5) == None:
            time2 = f"{hour2:02}:00"
        else:
            time2 = f"{hour2:02}:{time.group(5)}"

        # return in 24-hour format
        return f"{time1} to {time2}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()
