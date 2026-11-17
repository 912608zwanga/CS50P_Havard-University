def main():

    # Getting time from user
    clock = input("What time is it? ")
    #calling the convert()
    time = convert(clock)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print("snack time")


def convert(time):# receiving time

    # Hours , minutes
    hours, minutes = time.split(":")
    # convert time to float
    converted_minutes = float(minutes) / 60

    return float(hours) + converted_minutes


if __name__ == "__main__":
    main()
