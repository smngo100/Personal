# Functions: named blocks of code designed to do one specific job. When you want to perform particular task that you've defined in a function, you call the function responsible for it. 

# Defining a Function 
def greet_user():                   
  """Display a simple greeting."""  # Docstring: describes what the function does. A string used to document a Python module, class, function or method.
  print("Hello!")

greet_user() 
# Keyword def informs Python that you're defining a function 
# This is the function definition, which tells Pytthon the name of the fucntion and, if applicable, what kind of information the function needs to do its job. The parentheses hold that information.

# Passing Information to a Function 
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# Arguments and Parameters
# Parameter: A piece of information the function needs to do its job.
# Argument: A piece of informaiton that's passed from a function call to a function.
