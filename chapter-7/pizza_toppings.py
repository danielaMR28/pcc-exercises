prompt = "\nEnter a topping:"
prompt += "\nEnter 'quit' to end the program:"

topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Adding {topping} to your pizza!")