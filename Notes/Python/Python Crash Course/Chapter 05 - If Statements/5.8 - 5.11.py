# 5-8. Hello Admin
usernames = ['admin', 'mochiz', 'superdog', 'blueberry', 'creampuff']
user = input("What is your username? ").lower()

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# 5-9. No Users
usernames = []
if usernames:                                # if list is NOT empty, print statement     
    for username in usernames:
        print(f"Hello, {username}")    
else:                                        # Else, if list is empty, print statement
    print("We need to find some users!\n")   

# 5-10. Checking Usernames
current_users = ['mochiz', 'blueberry', 'pinecone', 'breadie', 'creampuff']
new_users = ['pineapple', 'popcorn', 'bloop', 'blueberry', 'creampuff']

# Need to make case-insensitive??
for new_user in new_users:
    if new_user in current_users:
        print("\nUser must enter a new username.")
    else:
        print(f"\nThe username {new_user} is available.")
        print("Creating username!")

# 5-11. Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
