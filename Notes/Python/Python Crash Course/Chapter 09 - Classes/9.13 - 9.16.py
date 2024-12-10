import random

# 9-13. Dice
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    # Method that prints a random number between 1 and 6
    def roll_die(self):
        random_num = random.randint(1, self.sides)
        print(f"Rolling a {self.sides} sided die: {random_num}")

# 6-sided die rolled 10 times
six_sided_die = Die()
for i in range(10):
    six_sided_die.roll_die()
print()

# 10-sided die rolled 10 times
ten_sided_die = Die(10)
for i in range(10):
    ten_sided_die.roll_die()
print()

# 20-sided die rolled 10 times
twenty_sided_die = Die(20)
for i in range(10):
    twenty_sided_die.roll_die()
print()


# 9-14. Lottery
# List containing a series of 10 numbers and 5 letters
series_of_num_letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
print("Any ticket matching these 4 numbers or letters win a prize: ")

winning_ticket = []
for i in range(4):
    # Randomly select 4 numbers or letters from the list
    ticket = random.choice(series_of_num_letters)
    winning_ticket.append(ticket)
    print(f"Winning tickets: {winning_ticket}")


# 9-15. Lottery Analysis
my_ticket = []
print("Pulling numbers until your ticket wins.")
while True:
    ticket = random.choice(series_of_num_letters)
    print(f"\tPulled ticket: {ticket}")

    if ticket in winning_ticket:
        print(f"{ticket} is a winning ticket!")
        break
    else:
        print("\tPull again.\n")


# 9-16. Python Module of the Week

series_of_num_letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
winning_tickets = []

while True:
    lottery_winners = random.choice(series_of_num_letters)

    print(f"Winning tickets: {lottery_winners}")
    winning_tickets.append(lottery_winners)

    print(f"Pulling numbers until your ticket wins.")
    if ticket in winning_ticket:
        print(f"{ticket} is a winning ticket!")
        break
    else:
        print("\tPull again.\n")
