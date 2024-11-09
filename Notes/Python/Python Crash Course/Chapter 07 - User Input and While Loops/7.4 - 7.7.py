# 7-4. Pizza Toppings
pizza_toppings = []
message = ""
while message != 'quit':
    message = input("\nEnter a pizza topping (or enter 'quit' to stop): ").lower()

    if message != 'quit':
        pizza_toppings.append(message)
        print(f"Adding {message} to pizza.")

"""
# Using a flag
active = True
while active:
    message = input("\nEnter a pizza topping (or enter 'quit' to stop): ").lower()

    if message == 'quit':
        active = False
    else:
        pizza_toppings.append(message)
        print(f"Adding {message} to pizza.")
"""

"""
# Using a break to Exit a Loop
message = ""
while True: 
    message = input("\nEnter a pizza topping (or enter 'quit' to stop): ").lower()
    
    if message == 'quit':
        break
    else: 
        pizza_toppings.append(message) 
        print(f"Adding {message} to pizza.")
"""

# 7-5. Movie Tickets
while True:
    age = int(input("\nEnter your age: "))

    if age < 3:
        ticket = "free"
        print(f"The cost of your movie ticket is free.")
    elif 3 <= age < 12:
        ticket = "10"
        print(f"The cost of your movie ticket is ${ticket}.")
    elif age > 12:
        ticket = "15"
        print(f"The cost of your movie ticket is ${ticket}.")
        break

# 7-6. Three Exists
pizza_toppings = []
message = ""

active = True
while active:
    message = input("\nEnter a pizza topping (or enter 'quit' to stop): ").lower()

    if message == 'quit':
        active = False
    else:
        pizza_toppings.append(message)
        print(f"Adding {message} to pizza.")

# 7-7. Infinity
x = 1
while x <= 5:
    print(x)
    # x += 1    if you omit this statement this will be an infinite loop bc x will start at 1 but never change. So the conditional test will always evaluate to True and the while loop will run forever.
