# Dictionary: A collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. 
# Note: A key's value can be a number, a string, a list, or even enother dictionary. Basically, you can use any object that you can create in Python as a value in a dictionary.
# A key-value pair is a set of values associated with each other.
# A dictionary is wrapped in braces {}

# Accessing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'] 
"""
Output:
green
"""

# Adding New Key-Value Pairs 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)
"""
Output:
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
"""

# Modifying Values in Dictionary
alien_0 = {'color': 'green}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"the alien is {alien_0['color']}.")
"""
Output: 
The alien is green.
The alien is yellow.
"""

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
"""
Output:
{'color': 'green', 'points': 5}
{'color': 'green'}
"""

