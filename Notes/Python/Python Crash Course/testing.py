from pathlib import Path 
import json

def get_stored_username(path): 
  if path.exists():
    contents = path.read_text()      # read contents from file 
    username = json.loads(contents)  # convert JSON formatted string into a Python object
    return username                  # return username 
  else: 
    return None

def get_new_username(path):
  username = input("What is your username? ")  # prompt user for username 
  contents = json.dumps(username)              # converts Python object to JSON formatted string
  path.write_text(contents)
  return username 
  
def greet_user():
  path = Path('username.json') 
  username = get_stored_username(path) 
  if username: 
    print(f"Welcome back, {username.title()}!)
  else: 
    username = get_new_username(path) 
    print(f"We'll remember you when you come back, {username.title()}!")

greet_user()
