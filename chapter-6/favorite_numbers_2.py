numbers = {
    'Ana' : [76,35], 
    'Sofia' : [78], 
    'Luci' : [22,865,345] , 
    'Juan' : [23,576,45745,746], 
    'Luis' : [0]
    }

for name, numeros in numbers.items():
    print(name.title(), ":")
    for  numero in numeros:
        print(f"\t{numero}")
