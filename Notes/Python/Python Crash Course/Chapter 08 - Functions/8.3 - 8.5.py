# 8-3. T-Shirt
def make_shirt(size, message):
    print(f"You are size {size}. The message on the shirt says '{message.title()}'.")

# Positional arguments
make_shirt('small', 'hello, world')

# Keyword arguments
make_shirt(size = 'small', message = 'hello, world')
print()

"""
Verbal interpretation: 
This code defines a function called make_shirt that takes two parameters: size and message. 
Inside the function, it prints a sentence that tells you your size and shows what message will be printed on the shirt. 
The message will be capitalized using .title().
Then, below the function definition, we actually call (or use) the function by passing in two arguments: 
'small' for the size and 'hello, world' for the message.
"""


# 8-4. Large Shirts
# Default values
def make_shirt(size = 'large', message = 'i love python'):
    print(f"You are size {size}. {message.title()}.")
make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'small', message = 'i love java')
print()


# 8-5. Cities
# Default value
def describe_city(city, country = 'the united states'):
    print(f"{city.title()} is in {country.title()}.")
describe_city('california')
describe_city('san diego')
describe_city(city = 'paris', country = 'france')
