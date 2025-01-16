# 11-1. City, Country 
"""
Write a function that accepts two parameters: a city name and a country name. 
The function should return a single string of the form City, Country, such as Santiago, Chile. 
Store the function in a module called city_functions.py, and save this file in a new folder so pytest won’t try to run the tests we’ve already written.
Create a file called test_cities.py that tests the function you just wrote. Write a function called test_city_country() to verify that calling your 
function with values such as 'santiago' and 'chile' results in the correct string. Run the test, and make sure test_city_country() passes.
"""

# Run test, and make sure test_city_country() passes
city_functions.py 
def get_formatted_city_country(city, country):
    city_country = f"{city}, {country}"
    return city_country.title()

test_cities.py 
from city_functions import get_formatted_city_country
def test_city_country():
    city_country =  get_formatted_city_country('santiago', 'chile')
    assert city_country == 'Santiago, Chile'

# In terminal, run the command "python -m pytest"


# 11-2. Population 
"""
Modify your function so it requires a third parameter, population. 
It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000. 
Run the test again, and make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run the test, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that verifies you can call your function with 
the values 'santiago', 'chile', and 'population=5000000'. Run the tests one more time, and make sure this new test passes.
"""

# Modify the function so that it requires a third parameter, population 
# Run the test again, and make sure test_city_country() fails this time. 
city_functions.py 
def get_formatted_city_country(city, country, population):
    city_country = f"{city.title()}, {country.title()} - population {population}"
    return city_country

test_cities.py 
from city_functions import get_formatted_city_country
def test_city_country():
    city_country =  get_formatted_city_country('santiago', 'chile')
    assert city_country == 'Santiago, Chile'


# Modify the function so the population parameter is optional. Run the test, and make sure test_city_country() passes again.
city_functions.py 
def get_formatted_city_country(city, country, population=''):
    if population:
        city_country = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country

test_cities.py 
from city_functions import get_formatted_city_country
def test_city_country():
    city_country =  get_formatted_city_country('santiago', 'chile', 5000000)
    assert city_country == 'Santiago, Chile - population 5000000'


# Second test called test_city_country_population() verifies that the user can call the function with the specific values. Run the test, and make sure this new test passes.
city_functions.py 
def get_formatted_city_country(city, country, population=''):
    if population:
        city_country = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country

test_cities.py 
from city_functions import get_formatted_city_country
def test_city_country():
    city_country =  get_formatted_city_country('santiago', 'chile')
    assert city_country == 'Santiago, Chile'

def test_city_country_population():
    city_country_population = get_formatted_city_country('santiago', 'chile', 5000000)
    assert city_country_population == 'Santiago, Chile - population 5000000'
