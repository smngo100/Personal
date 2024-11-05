# 7-1. Rental Car
rental_car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {rental_car.title()}.")

# 7-2. Restaurant Seating
people = int(input("How many people are in your dinner group? "))

if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

# 7-3. Multiples of Ten
number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
