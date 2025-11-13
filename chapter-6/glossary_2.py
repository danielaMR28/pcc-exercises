glossary = {
    'String' : 'A collection of letters', 
    'int' : 'An integer number', 
    'boolen' : 'True or False' , 
    'Python' : 'A programming language',
    'dictionary' : 'A set of key-value items',
    'value' : 'The one associated with a key', 
    'method' : 'A function that does something', 
    'print' : 'Used to print something in the console' , 
    'for' : 'A way of looping',
    'variable' : 'A value that changes',
    }

for terms in glossary:
    glossary.get(terms)
    print("\n", terms, ":", glossary[terms])