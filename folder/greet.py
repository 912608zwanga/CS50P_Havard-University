#return value

def greet(input):
  if "hello" in input:       #if hello is in the greet input function
    return "hello, there"    # it will print the response
  else:                # if its not in the input funtion
    return "I'm not sure what you mean"

#capture and use greet later on
greeting = greet("hello, computer") #hello is in the greet()
#greeting = greet("Hows you?") #hello is Not in the greet()
print(greeting)
