# 4-10. Slices
animals = ["wolf", "bear", "lion", "deer", "bobcat", "fox", "moose", "zebra"]
print(f"The first three items in the list are: {animals[:3]}.") # animals[0:3] would give same output
print(f"Three items from the middle of the list are: {animals[2:5]}.")
print(f"The last three items in the list are: {animals[5:]}\n")

# 4-11. My Pizzas, Your Pizzas
fav_pizzas = ["pineapple", "mushroom", "pepperoni"]
friend_pizzas = fav_pizzas[:]

fav_pizzas.append("cheese")
friend_pizzas.append("bbq")

print("My favorite pizzas are: ")
for fav_pizza in fav_pizzas:
    print(fav_pizza)
print()

print(f"My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
print()

# 4-12. More Loops
foods = ["pizza", "burger", "noodles", "rice", "soup", "steak", "fries"]
for food in foods:
    print(food)
