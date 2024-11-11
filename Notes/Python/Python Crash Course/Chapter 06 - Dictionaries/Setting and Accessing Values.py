# 7-8. Deli
sandwich_orders = ['tuna', 'reuben', 'turkey', 'ham']   # List with various sandwiches
finished_sandwiches = []                                # Empty list of finished sandwiches

while sandwich_orders:                                  # While there are still sandwiches in sandwich_orders
  making_sandwich = sandwich_orders.pop()               # Pop a sandwich as it is being made

  print(f"Making {making_sandwich} sandwich.")
  finished_sandwiches.append(making_sandwich)           # Append popped sandwich into finished_sandwiches

print("\nFinished making the following sandwiches: ")
for sandwich in finished_sandwiches:                    # Loop through finished_sandwiches
    print(f"I made your {sandwich} sandwich.")

# 7-9. No Pastrami
sandwich_orders = ['pastrami', 'tuna', 'reuben', 'pastrami', 'turkey', 'ham', 'pastrami']   # List of sandwiches but with multiple same sandwiches
print("\nThe deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:                    # While pastrami is still in sandwich_orders
    sandwich_orders.remove('pastrami')                  # Remove pastrami until there's none left

print(f"The following sandwiches are left: ")
for sandwich in sandwich_orders:                        # Loop through sandwich_orders
  print(f"{sandwich.title()} sandwich")

# 7-10. Dream Vacation
responses = {}                                          # Define an empty dictionary (responses)
polling_active = True                                   # Set a flag (polling_active) to indicate that polling is active.

while polling_active:                                   # As long as polling_active is True, Python wil run the code in the while loop.
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
             # Key    # Value
    responses[name] = response                          # Set user's response to responses dictionary
                                                        
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':                                  # If user's answer is no, polling ends
        polling_active = False

print(f"\n--- Poll Results ---")
for name, response in responses.items():                # for key, value in dictionary.items()
    print(f"{name.title()} would like to visit {response.title()}.")
