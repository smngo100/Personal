# 6-1. Person
person = {
    'first_name': 'john',
    'last_name': 'steel',
    'age': 23,
    'city': 'paris',
}

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'])

# 6-2. Favorite Numbers
fav_nums = {
    'kelly': 5,
    'mike': 25,
    'john': 19,
    'sally': 34,
    'bob': 27,
}
print(f"Kelly's favorite number is {fav_nums['kelly']}.")
print(f"Mike's favorite number is {fav_nums['mike']}.")
print(f"Johns's favorite number is {fav_nums['john']}.")
print(f"Sally's favorite number is {fav_nums['sally']}.")
print(f"Bob's favorite number is {fav_nums['bob']}.")

# 6-3. Glossary
glossary = {
    'string': 'letters',
    'comment': 'pound',
    'integer': 'number',
    'list': 'words',
    'float': 'decimal',
}
print(f"string: {glossary['string']}")
print(f"comment: {glossary['comment']}")
print(f"integer: {glossary['integer']}")
print(f"list: {glossary['list']}")
print(f"float: {glossary['float']}")
