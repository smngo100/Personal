# 8-15. Printing Models.
import printing_functions

printing_functions.print_models(unprinted_designs='phone case', 'robot pendant', 'dodecahedron')
#printing_functions.show_completed_models()


# 8-16. Imports.
import pizza
pizza.make_pizza(16, 'pepperoni')

from pizza import make_pizza
make_pizza(16, 'mushrooms')

from pizza import make_pizza as mp
mp(16, 'green peppers')

import pizza as pza
pza.make_pizza(16, 'pineapple')

from pizza import *
make_pizza(16, 'vegetables')

# 8-17. Styling Functions.
# The three programs follow the styling guidelines described in this section
