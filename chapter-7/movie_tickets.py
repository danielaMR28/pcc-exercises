prompt = "\nEnter your age:"

age = int(input(prompt))

while True:

    if age < 3:
        print("The ticket is free")
        break
    elif age >= 3 and age <= 12:
        print("The ticket is $10")
        break
    else:
        print("The ticket is $15")
        break
    
    age = 0