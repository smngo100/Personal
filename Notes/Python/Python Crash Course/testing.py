from pathlib import Path 
import json

def get_stored_username(path): 
  if path.exists():
    contents = path.read_text() 
    username = json.loads(contents) 
    return username 

def get_new_username(path):



def greet_user():
