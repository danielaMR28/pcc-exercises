numbers = {'Ana' : 76, 'Sofia' : 78, 'Luci' : 22 , 'Juan' : 23, 'Luis' : 0}

print(numbers)

people = {'Luci', 'Maria', 'Pedro', 'Ana', 'Monse'}

for person in people:
    if person in numbers:
        print("Thanks", f"{person}", "for responding")
    else:
        print(f"{person}", "please take the poll")