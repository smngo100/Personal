# 4-13. Buffet
foods = ("pizza", "sandwiches", "tacos", "burgers", "salad")    # Store five simple foods in tuple

# Print each food the restaurant offers
# For a tuple, you use a for loop as you would a list
for food in foods:
    print(food)
print()

# Error
# Why? Because tuples are immutable. Once you create a tuple you cannot modify it.
"""foods[0] = "steak"
print(foods)"""

# Overwriting
# You can't modify tuples, but you can assign a new value to a variable that represents a tuple.
foods = ('pizza', "sandwiches", "tacos", "fries", "steak")
for food in foods:
    print(food)
print()
