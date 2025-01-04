from pathlib import Path
import json

# **NOTE**: Creating a Path object creates a Python object that represents the path to that file

# 10-11. Favorite Number
"""Store user's favorite number in a file."""
fav_num = input("What is your favorite number? ")   # prompt user for their favorite number
path = Path('favorite_number.json')                 # create Path object for JSON file
contents = json.dumps(fav_num)                      # converts a Python object to JSON string format
path.write_text(contents)                           # write contents to the file

"""Load message about user's favorite number."""
path = Path('favorite_number.json')                 # create Path object for JSON file
contents = path.read_text()                         # read contents from file
fav_num = json.loads(contents)                      # converts JSON-formatted string into a Python object
print(f"I know your favorite number! It's {fav_num}.")


# 10-12. Favorite Number Remembered
"""Combined the two programs from Exercise 10-11."""
# If the number is already stored, report the favorite number to the user.
def get_stored_number(path):
    """Get stored number if available."""
    if path.exists():
        contents = path.read_text()
        fav_num = json.loads(contents)
        return fav_num
    else:
        return None

# If not, prompt the user's favorite number and store it in a file.
def get_new_number(path):
    """Prompt for a new number."""
    fav_num = input("What is your favorite number?")
    path = Path('favorite_number.json')
    contents = json.dumps(fav_num)
    path.write_text(contents)

def user_fav_num():
    """Get user's favorite number.'"""
    path = Path('favorite_number.json')
    fav_num = get_stored_number(path)
    if fav_num:
        print(f"I know your favorite number! It's {fav_num}.")
    else:
        fav_num = get_new_number(path)

user_fav_num()


# 10-13. User Dictionary
from pathlib import Path
import json

def get_stored_user_info(path):
    if path.exists():
        contents = path.read_text()         # read contents from file 
        user_info = json.loads(contents)    # converts JSON formatted string into a Python object
        return user_info
    else:
        return None

def get_new_user_info(path):
    username = input("What is your name? ")
    age = input("What is your age? ")
    job = input("What is your job? ")

    # Store collected information of the user in dictionary
    user_info = {'username': username, 'age': age, 'job': job}

    contents = json.dumps(user_info)    # converts a Python object into JSON formatted string 
    path.write_text(contents)           # write contents to file 
    return user_info

def greet_user():
    path = Path('user_info.json')           # create Path object for JSON file 
    user_info = get_stored_user_info(path) 
    if user_info:
        print(f"Welcome back, {user_info['username'].title()}! You're {user_info['age']} years old and work as a {user_info['job']}.")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back!\nName: {user_info['username'].title()}\nAge: {user_info['age']}\nJob: {user_info['job'].title()}")

greet_user()


# 10-14. Verify User





