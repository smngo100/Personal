# 6-7. People
# A list of dictionaries 
person_1 = {
    'first': 'john',
    'last': 'steel',
    'age': 23,
    'city': 'paris',
}

person_2 = {
    'first': 'sally',
    'last': 'maine',
    'age': 29,
    'city': 'houston'
}

person_3 = {
    'first': 'mike',
    'last': 'boe',
    'age': 32,
    'city': 'seattle'
}

persons = [person_1, person_2, person_3]

for person in persons:
    print(f"{person['first'].title()} {person['last'].title()} is {person['age']} years old and lives in {person['city'].title()}.")

# 6-8. Pets
# A list of dictionaries 
dog = {
    'animal': 'dog',
    'owner': 'bob',
}

cat = {
    'animal': 'cat',
    'owner': 'sally',
}

bird = {
    'animal': 'bird',
    'owner': 'mike',
}

pets = [dog, cat, bird]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']}.")

# 6-9. Favorite Places
# A list in a dictionary
favorite_places = {
    'bob': ['paris', 'new york', 'philadelphia'],
    'sally': ['houston', 'boston'],
    'mike': ['seattle'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are: ")
    else:
        print(f"\n{name.title()}'s favorite place is: ")

    for place in places:
        print(f"\t{place.title()}")

# 6-10. Favorite Numbers
# A list in a dictionary
fav_nums = {
    'kelly': [5, 20, 48],
    'mike': [25, 14, 56],
    'john': [19, 5],
    'sally': [34, 45],
    'bob': [27, 1, 15],
}

for name, numbers in fav_nums.items():
    print(f"\n{name.title()}'s favorite numbers are: ")

    for number in numbers:
        print(f"\t{number}")

# 6-11. Cities
# A dictionary in a dictionary
cities = {
    'paris': {
        'country': 'france',
        'population': 2162277,
        'fact': 'the capital of France',
    },

    'new york': {
        'country': 'usa',
        'population': 8403353,
        'fact': 'the capital of USA',
    },

    'ottawa': {
        'country': 'canada',
        'population': 2347811,
        'fact': 'the capital of Canada',
    },

}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country_population_fact = f"{city.title()}, {city_info['country'].title()} has a population of {city_info['population']} and is {city_info['fact']}."

    print(f"\t{country_population_fact}")

# 6-12. Extensions
# Do
