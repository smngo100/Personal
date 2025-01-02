# 10-4. Guest
from pathlib import Path

guest = input("What is your name? ").title()

path = Path('guest.txt')
path.write_text(guest)
print()

# 10-5. Guest Book
while True:
    guest = input("What is your name? ").title()

    if guest.lower() == 'quit':
        break
    else:
        with open('guest_book.txt', 'a') as file:
            file.write(guest + '\n')
