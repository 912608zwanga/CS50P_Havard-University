# import necessary module
import random

# Loop forever until a valid level is entered
while True:
    try:
        # Get user input for level
        level = int(input("Level: "))

        # Check if level is positive
        if level > 0:
            # Generate a random value between 1 and the level
            value = random.randint(1, level)
            break
        else:
            # If negative or zero, reprompt
            continue

    except ValueError:
        # If input is not an integer, reprompt
        continue

# Loop forever for the user's guesses
while True:
    try:
        # Get user input for the guess
        guess = int(input("Guess: "))

    except ValueError:
        # If input is not an integer, reprompt
        continue

    else:
        # Check if guess is less than or equal to 0
        if guess <= 0:
            continue

        # Check if guess is smaller than the random value
        elif guess < value:
            print("Too small!")

        # Check if guess is larger than the random value
        elif guess > value:
            print("Too large!")

        # Otherwise, the guess is correct
        else:
            print("Just right!")
            # Stop the while loop
            break
