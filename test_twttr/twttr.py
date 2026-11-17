def main():
    # Get user input
    word = input("Input: ")
    # Print the shortened version
    print("Output:", shorten(word))


def shorten(word):
    # Use translate and maketrans to remove all vowels (upper and lower)
    # The third argument in maketrans specifies characters to be deleted
    return word.translate(str.maketrans("", "", "aeiouAEIOU"))


if __name__ == "__main__":
    main()
