# User input
answer = input("Input: ")

# Print Output
print("Output: ", end="")

# Loop through every letter
for letter in answer:
    # Check if it is not a vowel (uppercase or lowercase)
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        # Print the letter
        print(letter, end="")

# Print new line
print()
