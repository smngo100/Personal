# Functions: named blocks of code designed to do one specific job. When you want to perform particular task that you've defined in a function, you call the function responsible for it. 

# Defining a Function 
def greet_user():                   
  """Display a simple greeting."""  # Docstring: describes what the function does. A string used to document a Python module, class, function or method.
  print("Hello!")

greet_user()   # function call: tells Python to execute the code in the function
# Keyword def informs Python that you're defining a function 
# This is the function definition, which tells Pytthon the name of the fucntion and, if applicable, what kind of information the function needs to do its job. The parentheses hold that information.

# Passing Information to a Function 
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

"""
Arguments and Parameters
- Parameter: A piece of information the function needs to do its job.
- Argument: A piece of informaiton that's passed from a function call to a function.
"""

# Passing Arguments 
  # Positional arguments: need to be in the same order the parameters were written 
  # Keyword arguments: each argument consists of a variable name and a value

# Positional Arguments 
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
# The definition shows function needs a type of animal and the animal's name
  # Need to provide an animal type and name in that order

# Keyword Arguments 
  # Keyword argument: a name-value pair that you pass to a function 
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

# Default Values 
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
# *Note*: When you use default values, any parameter with a default value needs to be listed after all the parameters taht don't have default values. 
# . . . So that Python can continue interpreting positional arguments correctly.

# Return Values
# Return value: The value the function returns
# return statement takes a value from inside a function and sends it back to the line that called the function

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional 
# To make argument optional, give the argument an empty default value and ignore the the argument unless the user provides a value 
# set the default value of the argument to an empty string and move it to the end of the list of parameters 

# 
