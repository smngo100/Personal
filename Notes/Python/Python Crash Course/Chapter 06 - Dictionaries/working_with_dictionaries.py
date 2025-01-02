# Dictionary: A collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. 
# Note: A key's value can be a number, a string, a list, or even enother dictionary. Basically, you can use any object that you can create in Python as a value in a dictionary.
# A key-value pair is a set of values associated with each other.
# A dictionary is wrapped in braces {}
# Note: get() is a method for dictionaries

# Accessing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])


# Adding New Key-Value Pairs 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)


# Modifying Values in Dictionary
# Think of it as basically overwriting the value
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")


# See it overwrites it here with 'yellow'
alien_0['color'] = 'yellow'
print(f"the alien is {alien_0['color']}.")


# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


# Using get() to Access Values 
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])


# Use the get() method. It requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn't exist. If you call .get with just one argument, the key, the default value is None).
"""
get() method syntax: dictionary.get(keyname, value) 
keyname: Required. The keyname of the item you want to return the value from.
value: Optional. A value to return if the specified key does not exist. Default value is None.
"""

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


# Looping Through All Key-Value Pairs 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")
# The key is assigned to the variable name, and the value is assigned to the variable language.


# Looping Through All the Keys in a Dictionary 
# The keys() method is useful when you don't need to work with all of the values in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name in favorite_languages.keys():
  print(name.title())
  # Looping through the keys is the default behavior when looping through a dictionary, so this code would have the same output if you wrote for name in favorite_languages


# Looping Through a Dictionary's Keys in a Particular Order
# Can use the sorted() method to temporarily sort the keys order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")


# Looping Through All the Values in a Dictionary 
# The values() method returns a sequence of values without any keys.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for language in favorite_languages.values():
  print(language.title())


# Using a set() 
# A set is a collection in which each item must be unique.
# set() wraps around a collection of values
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
  print(language.title())
