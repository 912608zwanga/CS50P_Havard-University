# Get user inputs
camelCase = input("CamelCase: ")
snake_case = ""
# print "snake_case"
print("snake_case: ", end="")

# Loop through every letter
for letter in camelCase:
    # check if letter is uppercase
    if letter.isupper():
        # print underscore and letter in lowercase
        print("_" + letter.lower(), end="")

    else:
        # otherwise, print letter
        print(letter, end="")

# print space in the end
print()
