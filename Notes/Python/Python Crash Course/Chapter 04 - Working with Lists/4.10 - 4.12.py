# In silcing, when you include an end value, it excluse that value when printed. 

# 4-10. Slices
animals = ["wolf", "bear", "lion", "deer", "bobcat", "fox", "moose", "zebra"]
print(f"The first three items in the list are: {animals[:3]}.")    # animals[0:3] would give same output    # Here, it excludes the element at index 3. It will print "worlf", "bear", "lion", but not the last element "deer"
print(f"Three items from the middle of the list are: {animals[2:5]}.")
print(f"The last three items in the list are: {animals[5:]}\n")    # Here, it will print at index 5 and the rest of the elements in the list           


# 4-11. My Pizzas, Your Pizzas
fav_pizzas = ["pineapple", "mushroom", "pepperoni"]
friend_pizzas = fav_pizzas[:]  # Make a copy of the list of pizzas

fav_pizzas.append("cheese")    # Add a new pizza to the original list 
friend_pizzas.append("bbq")    # Add a different pizza to the list friend_pizzas

# Prove you have two separate lists 
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
