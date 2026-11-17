# Prompt user for input
Question = "What is the Great Question of Life, the Universe and Everything? "
Answer = input(Question)

# Check if the answer is correct
if Answer.strip() == "42": # Using strip() to remove any leading or trailing whitespace
    print("Yes")
elif Answer.strip().lower() == "forty-two":
    print("Yes")
elif Answer.strip().lower() == "forty two":
    print("Yes")
else:  # If the answer is not correct
    print("No")
