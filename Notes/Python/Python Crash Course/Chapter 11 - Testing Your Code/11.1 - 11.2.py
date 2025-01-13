# 11-1. City, Country 
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
