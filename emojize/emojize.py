import emoji

# Get user input
n = input("Input: ")

# Convert the alias into an emoji
# We use language='alias' to support codes like :thumbsup:
output = emoji.emojize(n, language='alias')

# Print the result
print("Output:", output)
