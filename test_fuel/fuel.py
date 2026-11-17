def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split('/')
    try:
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    # ADD THIS: Check if either number is negative
    if x < 0 or y < 0:
        raise ValueError

    if x > y:
        raise ValueError

    fuel = round(x / y * 100)
    return fuel

def gauge(percentage):
    # If fuel is 99% or more, show 'F' for Full
    if percentage >= 99:
        return 'F'
    # If fuel is 1% or less, show 'E' for Empty
    elif percentage <= 1:
        return 'E'
    # Otherwise, show the actual percentage
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
