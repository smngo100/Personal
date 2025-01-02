from pathlib import Path
import json

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
def get_stored_number(path):
    """Get stored number if available."""
    if path.exists():
        contents = path.read_text()
        fav_num = json.loads(contents)
        return fav_num
    else:
        return None

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






# 10-14. Verify User





# Creating a Path object creates a Python object that represents the path to that file
