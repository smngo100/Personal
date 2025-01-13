# 11-1. City, Country 
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



