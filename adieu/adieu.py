# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
import inflect

# Create an inflect engine instance
p = inflect.engine()

# Create an empty list to store only the names entered by the user
names = []

# Loop forever to collect names
while True:
    try:
        # Get user input for names
        n = input("Name: ")
        # Add the name to our list
        names.append(n)

    except EOFError:
        # When user presses Ctrl-D, print a blank line and exit loop
        print()
        break

# Use p.join to handle the grammar (commas and the word "and")
# This handles 1, 2, or 100 names automatically
formatted_names = p.join(names)

# Print the final combined string
# We print the greeting first, followed by the formatted list
print("Adieu, adieu, to", formatted_names)
