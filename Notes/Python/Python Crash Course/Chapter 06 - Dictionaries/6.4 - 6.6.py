# 6-4. Glossary 2
glossary = {
    'object': 'variable',
    'class': 'blueprint',
    'method': 'function',
    'string': 'characters',
    'module': 'file'
    }

# Add 5 more Python terms to the glossary
glossary['list'] = 'mutable'
glossary['tuple'] = 'immutable'
glossary['append'] = 'add'
glossary['float'] = 'decimal'
glossary['integer'] = 'whole number'

for term, definition in glossary.items():
    print(f"\nTerm: {term.title()}")
    print(f"Definition: {definition.title()}")
print()


# 6-5. Rivers
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print()


# 6-6. Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
if 'sally' not in favorite_languages.keys():
    print("Sally, please take our poll!")
if 'john' not in favorite_languages.keys():
    print("John, please take our poll!\n")
for name in favorite_languages.keys():
    print(f"Thank you {name.title()} for taking our poll!")

# Another way to do it
"""user = input("Enter your name: ")
if user not in favorite_languages.keys():
    print(f"{user.title()}, please take our poll!")
for name in favorite_languages.keys():
    print(f"Thank you {name.title()} for taking our poll!")"""
