import random

# Global list of valid levels
levels = [1, 2, 3]

def main():
    # Set total problems, initial score, and get level
    score = 0
    level = get_level()

    # Randomly generates ten (10) math problems
    for _ in range(10):
        val1 = generate_integer(level)
        val2 = generate_integer(level)
        trial = 0

        # Allow up to three tries in total for that problem
        while trial < 3:
            try:
                answer = int(input(f"{val1} + {val2} = "))

                if answer == (val1 + val2):
                    # Correct answer
                    score += 1
                    break
                else:
                    # Incorrect answer
                    print("EEE")
                    trial += 1
            except ValueError:
                # Not even a number
                print("EEE")
                trial += 1

        # After three incorrect answers, display the correct answer
        if trial == 3:
            print(f"{val1} + {val2} = {val1 + val2}")

    # Output the user's score
    print(f"Score: {score}")


def get_level():
    # Prompts the user for a level, n (1, 2, or 3)
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # Returns a randomly generated non-negative integer with n digits
    if level not in levels:
        raise ValueError

    if level == 1:
        # Single digit includes 0 to 9
        return random.randint(0, 9)
    else:
        # level 2: 10 to 99, level 3: 100 to 999
        start = 10**(level - 1)
        end = (10**level) - 1
        return random.randint(start, end)


if __name__ == "__main__":
    main()
