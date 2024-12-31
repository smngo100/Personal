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
"""Code adapted from Exercise 10-5 adapted so the user can continue entering numbers."""
while True:
    num1 = input("Enter first number: ")
    if num1 == 'q':
        break
    try:
        num1 = int(num1)
    except ValueError as e:
        print(e, "\n")

    num2 = input("Enter second number: ")
    if num2 == 'q':
        break
    try:
        num2 = int(num2)
        result = int(num1) + int(num2)
    except ValueError as e:
        print(e, "\n")
    else:
        print(f"Result: {result}\n")


# 10-8. Cats and Dogs
"""Reads contents of cat and dog files and prints a friendly message if a file is missing."""

path_cat = Path('cats.txt')
path_dog = Path('dogs.txt')

# Cat contents
try:
    cat_contents = path_cat.read_text().title()
except FileNotFoundError:
    print(f"The file {path_cat} does not exist.")
else:
    print(f"Cat names: \n{cat_contents}\n")

# Dog contents
try:
    dog_contents = path_dog.read_text().title()
except FileNotFoundError:
    print(f"The file {path_dog} does not exist.")
else:
    print(f"Dog names: \n{dog_contents}\n")


# 10-9. Silent Cats and Dogs
"""Modifies Exercise 10-8 to fail silently if either file is missing."""
# To fail silently when an exception occurs and continue on as if nothing happened just use a pass statement. It tells Python to do nothing in a block.
path_cat = Path('cats.txt')
path_dog = Path('dogs.txt')

# Cat contents
try:
    cat_contents = path_cat.read_text().title()
except FileNotFoundError:
    pass
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
