# 4-13. Buffet
foods = ("pizza", "sandwiches", "tacos", "burgers", "salad")    # Store five simple foods in tuple

# Print each food the restaurant offers
for food in foods:
    print(food)

# Error
"""foods[0] = "steak"
print(foods)"""

# Overwriting
foods = ('pizza', "sandwiches", "tacos", "fries", "steak")
for food in foods:
    print(food)
