# Getting user input
greetings = input("What is your greeting? ").strip()

if greetings.startswith("hello") or greetings.startswith("Hello") or greetings.startswith("HELLO"):
    print("$0")

elif greetings.startswith("h") or greetings.startswith("H") :
    print("$20")
else:
    print("$100")
