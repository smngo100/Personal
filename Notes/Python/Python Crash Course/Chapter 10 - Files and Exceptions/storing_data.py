"""JSON (JavaScript Object Notation) allows you to convert simple Python data structures into JSON-formatted strings,
and then load the data from that file the next time the program runs. """

from pathlib import Path
import json

##### json.dumps() and json.loads()
# json.dumps() takes one argument: a piece of data that should be converted to the JSON format
    # The function returns a string, which we can then write to a data file.
numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
contents = json.dumps(numbers)  # Converts numbers to the JSON format
path.write_text(contents)

# json.loads() reads the data from json.dumps() back into memory
path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)


##### Saving and Reading User-Generated Data
# Storing the user's name
username = input("\nWhat is your name? ").title()

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")

# Greeting a user whose name has already been stored
path = Path('username.json')
contents = path.read_text()
user = json.loads(contents)
print(f"\nWelcome back, {user}!")


##### Refactoring #####
"""Refactoring is when you could improve code by breaking it up into a series of functions that have specific jobs. 
It makes your code cleaner, easier to understand, and easier to extend."""
# Refer to remember_me.py for refactoring (basically just moved all the code into a function
