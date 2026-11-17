import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    # Check the command line arguments
    check_command_line_arg()

    # Open the image (the muppet/person image provided as sys.argv[1])
    try:
        user_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open shirt (the overlay image provided by CS50)
    shirt = Image.open("shirt.png")

    # Get the size of the shirt
    size = shirt.size

    # Resize muppet image to fit shirt
    # fit() crops and resizes the user image to match the shirt's dimensions
    user_image = ImageOps.fit(user_image, size)

    # Paste shirt in muppet
    # The shirt has transparency, so we use it as the third argument (mask)
    user_image.paste(shirt, shirt)

    # Create output image
    user_image.save(sys.argv[2])


def check_command_line_arg():
    # Check how many elements in the command line (expects input and output names)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if it is an Image file (must be .jpg, .jpeg, or .png)
    valid_extensions = [".jpg", ".jpeg", ".png"]
    extension1 = splitext(sys.argv[1].lower())[1]
    extension2 = splitext(sys.argv[2].lower())[1]

    if extension2 not in valid_extensions:
        sys.exit("Invalid output")

    # Check if extension of both files are the same
    if extension1 != extension2:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
