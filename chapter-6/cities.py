cities = {
    "Mexico City" : {"Country" : "Mexico", "Population" : 22000000, "Fact" : "It has a lot of traffic"},
    "Rome" : {"Country" : "Italy", "Population" : 4000000, "Fact" : "It's beatiful"},
    "Athens" : {"Country" : "Greece", "Population" : 3000000, "Fact" : "A lot of culture"}
    }

for city, city_info in cities.items():
    print("City:", city)
    print("     Country:", city_info['Country'])
    print("     Population:", city_info['Population'])
    print("     Fact:", city_info['Fact'])