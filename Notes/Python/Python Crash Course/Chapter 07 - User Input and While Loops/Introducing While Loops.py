# Recall: The for loop takes a collection of items and executes a block of code once for each item in the collection. 
# The while loop runs as along as, or while, a certain condition is true. 

# Using a Flag
# For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value fo the flag to False.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
  message = input(prompt)
  
  if message == 'quit':
      active = False
  else:
      print(message)

# Using break to Exit a Loop 
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
  city = input(prompt)

  if city == 'quit':
      break
  else:
      print(f"I'd love to go to {city.title()}!")

"""
---------- KEY DIFFERENCES BETWEEN A FLAG AND BREAK ---------- 
1. Readability: 
* With a flag, you can clearly see that the loop's execution is contingent upon the value of active.
* The break statement makes it clear that the loop will terminate upon satisfying a specific condition.

2. Exit Conditions: 
* Using a flag can make sense when there are multiple conditions that might end the loop since you can set the flag from different points in the loop.
* A break statement is more straightforward for a single exit condition.

3. Code Structure: 
* Flags are useful for loops with complex exit conditions where the decision to exit can depend on multiple factors and might be set at various points within the loop.
* Break statements are cleaner for simple, single-condition exits, reducing the need for additional variables.
"""

# Using continue in a Loop
# The continue statement returns to the beginning of the loop

# Using a while loop with Lists and Dictionaries 
# A for loop is effective for looping through a list, but you shoudlnt' modify a list inside a for loop. To modify a list as you work through it, use a while lop. 
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"\nThe following users have been confirmed: ")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing All Instance of Specific Values from a List
