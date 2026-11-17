def main():
    # get user input
    say = input('Do have something to say? ')
    # call convert ()
    result = convert(say)
    # print the results
    print(result)

def convert(say):
    # Replace :) with a happy emoji
    say1 = say.replace(":)", '🙂')

    # Replace :( with a frowning emoji
    say2 = say1.replace(":(", '🙁')

    #retun string
    return say2

main()
