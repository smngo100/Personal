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
sandwich_orders = ['pastrami', 'tuna', 'reuben', 'pastrami', 'turkey', 'ham', 'pastrami']
print("\nThe deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"The following sandwiches are left: ")
for sandwich in sandwich_orders:
  print(f"{sandwich.title()} sandwich")


# 7-10. Dream Vacation
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print(f"\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
