def get_guess(): #define Function called get_guess()
    guess = int(input("Enter a guess : "'\n')) # prompt the to enter a guess
    return guess # return value

#print(get_guess()) # run the guess


def main():
    # guess variable can be used multiple times, its in different functions/Scopes
    guess = get_guess()
    if guess == 50:
        print("Correct")
    else:
        print("Incorrect")

main()
