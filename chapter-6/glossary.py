glossary = {
    'String' : 'A collection of letters', 
    'int' : 'An integer number', 
    'boolen' : 'True or False' , 
    'Python' : 'A programming language',
    'Dictionary' : 'A set of key-value items',
    }

for terms in glossary:
    glossary.get(terms)
    print("\n", terms, ":", glossary[terms])


