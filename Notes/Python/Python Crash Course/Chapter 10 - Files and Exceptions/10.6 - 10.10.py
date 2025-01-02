from pathlib import Path

# 10-6. Addition
"""Prompts user for two numbers and prints the result."""
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
except ValueError as e:
    print(e)
else:
    print(f"Result: {result}")
print()


# 10-7. Addition Calculator
"""Code from Exercise 10-5 adapted so the user can continue entering numbers."""
while True:
    num1 = input("Enter first number: ")
    if num1 == 'quit':
        break
    try:
        num1 = int(num1)
    except ValueError as e:
        print(e, "\n")

    num2 = input("Enter second number: ")
    if num2 == 'quit':
        break
    try:
        num2 = int(num2)
        result = int(num1) + int(num2)
    except ValueError as e:
        print(e, "\n")
    else:
        print(f"Result: {result}\n")
print()

# 10-8. Cats and Dogs
"""Reads contents of cat and dog files and prints a friendly message if a file is missing."""

path_cat = Path('cats.txt')
path_dog = Path('dos.txt')  # Misspelled file

print("----- Cat and Dog names with exception message -----")
# Cat contents
try:
    cat_contents = path_cat.read_text().title()
except FileNotFoundError:
    print(f"The file {path_cat} does not exist.\n") # This one shows the message
else:
    print(f"Cat names: \n{cat_contents}\n")

# Dog contents
try:
    dog_contents = path_dog.read_text().title()
except FileNotFoundError:
    print(f"The file {path_dog} does not exist.\n")
else:
    print(f"Dog names: \n{dog_contents}\n")


# 10-9. Silent Cats and Dogs
"""Modifies Exercise 10-8 to fail silently if either file is missing."""
# To fail silently when an exception occurs and continue on as if nothing happened just use a pass statement.
# It tells Python to do nothing in a block.

path_cat = Path('cas.txt')  # Misspelled file
path_dog = Path('dogs.txt')

print("----- Cat and Dog names fail silently -----")
# Cat contents
try:
    cat_contents = path_cat.read_text().title()
except FileNotFoundError:
    pass    # Fails silently
else:
    print(f"Cat names: \n{cat_contents}\n")

# Dog contents
try:
    dog_contents = path_dog.read_text().title()
except FileNotFoundError:
    pass
else:
    print(f"Dog names: \n{dog_contents}\n")


# 10-10. Common Words
"""Analyze file: word count, line count, and word frequency."""

path = Path('moby_dick.txt')
contents = path.read_text(encoding='utf-8')

# Word count
words = contents.split()
num_words = len(words)
print(f"The file {path} has about {num_words} words.")

# Line count
lines = contents.splitlines()
num_lines = len(lines)
print(f"The file {path} has about {num_lines} lines.")

# Amount of times the word 'the' appears in each text
the = words.count('the')
print(f"Word count of 'the': {the}")

# 'the ' with a space in the string
the_w_space = contents.count('the ')
print(f"Word count of 'the ': {the_w_space}")
