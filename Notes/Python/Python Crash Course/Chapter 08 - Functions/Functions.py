# Functions: named blocks of code designed to do one specific job.
# When you want to perform particular task that you've defined in a function, you call the function responsible for it.
# ***** EVERY FUNCTION HAS ONE SPECIFIC JOB *****

"""
Arguments and Parameters
- Parameter: A piece of information the function needs to do its job.
- Argument: A piece of informaiton that's passed from a function call to a function.
"""


##### Defining a Function #####
def greet_user():  # This is the function definition, which tells Python the name of the function and, if applicable, what kind of information the function needs to do its job. The parentheses hold that information.
    """Display a simple greeting."""  # Docstring: describes what the function does. A string used to document a Python module, class, function or method.
    print("Hello!")

greet_user()  # function call: tells Python to execute the code in the function

# Keyword def informs Python that you're defining a function

# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')


########## Passing Arguments ##########
# Positional arguments: need to be in the same order the parameters were written
# Keyword arguments: each argument consists of a variable name and a value

##### Positional Arguments #####
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
# The definition shows function needs a type of animal and the animal's name
# Need to provide an animal type and name in that order

##### Keyword Arguments #####
# Keyword argument: a name-value pair that you pass to a function
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')


##### Default Values #####
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')


# *Note*: When you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values.
# So that Python can continue interpreting positional arguments correctly.

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
# To make argument optional, give the argument an empty default value and ignore the argument unless the user provides a value
# set the default value of the argument to an empty string and move it to the end of the list of parameters

# Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


# Returning a Dictionary with Optional Values
# Optional value here is 'age'
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print(f"\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


# Passing a List
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# Modifying a List in a Function
def print_models(unprinted_designs, completed_models):  # Handles printing the designs
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing mode: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):  # Summarizes the prints that have been made
    print(f"\n The following models that were printed.")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
# Send a copy of a list to a function
function_name(list_name[:])  # Slice notation makes a copy of the list to send to the function


# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# * asterisk collects as many arguments as the calling line provides
# * asterisk in the parameter name *toppings tells Python to make a tuple called toppings, containing all the values this function receives

# ** double asterisks tells Python to createa a dictionary containing all the extra name-value pairs the function receives
# You'll often see the parameter name **kwargs used to collect nonspecific keyword arugments

"""
If you specify a default value for a parameter, no spaces should be used on either side of the equal sign:

  def function_name(parameter_0, parameter_1='default value')


The same convention should be used for keyword arguments in function calls:

  function_name(value_0, parameter_1='value')

"""
