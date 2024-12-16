# 7-4. Pizza Toppings
pizza_toppings = [] # Define empty list pizza toppings   
message = ""        # Define as an empty string so Python has something to check the first time it reaches the while line 
while message != 'quit':    # While message is not quit
    message = input("\nEnter a pizza topping (or enter 'quit' to stop): ").lower()

    if message != 'quit':
        pizza_toppings.append(message)
        print(f"Adding {message} to pizza.")
    
"""
print("You added to your pizza: ") 
for pizza_topping in pizza_toppings: 
print("\t" + pizza_topping) 
"""

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
        #break 
    elif 3 <= age < 12:
        ticket = "10"
        print(f"The cost of your movie ticket is ${ticket}.")
        #break 
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
