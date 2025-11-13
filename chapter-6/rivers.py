rivers = {
    'nile' : 'egypt', 
    'amazon' : 'brazil', 
    'mississippi' : 'united states' , 
    'yellow river' : 'china',
    'yangtze' : 'china',
    }

for river in rivers:
    print("\n The", f"{(river).title()} runs through", f"{(rivers[river]).title()}")
    
for river in rivers:
    print("\n", river.title())

for country in rivers:
    print("\n", rivers[country].title())