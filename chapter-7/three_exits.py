prompt = "\nEnter a topping (You can only add 3 ingredients):"

topping = ""
x = 0

while x < 3 and topping != 'test':
    topping = input(prompt)

    if topping == 'quit':
        break

    elif topping != 'test':
        print(f"Adding {topping} to your pizza!")
        x = x + 1
