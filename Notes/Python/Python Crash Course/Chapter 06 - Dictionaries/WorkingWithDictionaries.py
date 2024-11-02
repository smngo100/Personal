# Dictionary: A collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. 
# Note: A key's value can be a number, a string, a list, or even enother dictionary. Basically, you can use any object that you can create in Python as a value in a dictionary.
# A key-value pair is a set of values associated with each other.
# A dictionary is wrapped in braces {}
# Note: get() is a method for dictionaries

# Accessing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])
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
# Think of it as basically overwriting the value
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

# See it overwrites it here with 'yellow'
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

# Using get() to Access Values 
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])
"""
Output: 
Traceback (most recent call last):
  File "alien_no_points.py", line 2, in <module>
    print(alien_0['points'])
          ~~~~~~~^^^^^^^^^^
KeyError: 'points'
"""

# Use the get() method. It requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn't exist.
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
"""
Output:
No point value assigned.
"""
