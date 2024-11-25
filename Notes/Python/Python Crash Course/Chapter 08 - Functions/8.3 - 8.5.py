# 8-3. T-Shirt
def make_shirt(size, message):
    print(f"You are size {size}. The message on the shirt says '{message.title()}'.")

# Positional arguments
make_shirt('small', 'hello, world')

# Keyword arguments
make_shirt(size = 'small', message = 'hello, world')


# 8-4. Large Shirts
def make_shirt(size = 'large', message = 'i love python'):
    print(f"You are size {size}. {message.title()}.")
make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'small', message = 'i love java')


# 8-5. Cities
def describe_city(city, country = 'the united states'):
    print(f"{city.title()} is in {country.title()}.")
describe_city('california')
describe_city('san diego')
describe_city(city = 'paris', country = 'france')
