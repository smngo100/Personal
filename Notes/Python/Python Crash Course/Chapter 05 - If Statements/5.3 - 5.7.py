# 5-3. Alien Colors #1
alien_color = 'green'

# Passes test
if alien_color == 'green':
    print("Player just earned 5 points")

# Fails test
aline_color = 'red'
if alien_color == 'green':
    print("Player did not earn points")


# 5-4. Alien Colors #2
alien_color = 'red'

if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")


# 5-5. Alien Colors #3
alien_color = input("\nWhat is the alien's color? ").lower()
if alien_color == 'green':
    print("Player just earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")


# 5-6. Stages of Life
age = int(input("\nHow old are you? "))

# Multiple print calls
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# Another way to do it, but more concise with a single print() call
if age < 2:
    status = "baby"
elif age < 4:
    status = "toddler"
elif age < 13:
    status = "kid"
elif age < 20:
    status = "teenager"
elif age < 65:
    status = "adult"
else:
    status = "elder"

print(f"The person is a/an {status}.\n")


# 5-7. Favorite Fruit
favorite_fruits = ["mango", "watermelon", "grapes", "blueberries", "cherries"]

if "mango" in favorite_fruits:
    print("You really like mango!")
if "strawberries" in favorite_fruits:
    print("You really like strawberries!")
if "grapes" in favorite_fruits:
    print("You really like grapes!")
if "watermelon" in favorite_fruits:
    print("You really like watermelon!")
if "apples" in favorite_fruits:
    print("You really like apples!")
