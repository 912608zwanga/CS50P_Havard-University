from pyfiglet import Figlet
import sys
import random

# Create an instance of Figlet
figlet = Figlet()

# list of fonts
fonts = figlet.getFonts()

# Check for correct number of command-line arguments
if len(sys.argv) == 1:
    # If 0 arguments, choose a random font
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    # If 2 arguments, check if the first is -f or --font
    # And check if the second is a valid font name
    if sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

else:
    # Otherwise, exit the program
    sys.exit("Invalid usage")

# Get user input
text = input("Input: ")

# Print the rendered text
print(figlet.renderText(text))
