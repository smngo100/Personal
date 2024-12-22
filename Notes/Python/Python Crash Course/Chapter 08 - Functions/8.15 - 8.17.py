# 8-15. Printing Models.
import printing_functions

printing_functions.print_models(unprinted_designs='phone case', 'robot pendant', 'dodecahedron')
#printing_functions.show_completed_models()


# 8-16. Imports.
# Importing an entire module
import pizza
pizza.make_pizza(16, 'pepperoni')

# Importing a specific function from a module
from pizza import make_pizza
make_pizza(16, 'mushrooms')

# Importing a function from a module as an alias
from pizza import make_pizza as mp
mp(16, 'green peppers')

# Importing a module as an alias 
import pizza as pza
pza.make_pizza(16, 'pineapple')

# Importing all functions in a module 
from pizza import *
make_pizza(16, 'vegetables')


# 8-17. Styling Functions.
# The three programs follow the styling guidelines described in this section
