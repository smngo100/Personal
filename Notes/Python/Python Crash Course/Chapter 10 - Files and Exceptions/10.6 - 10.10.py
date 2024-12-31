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
path_cat = Path('cats.txt')
path_dog = Path('dogs.txt')

cat_contents = path_cat.read_text()
dog_contents = path_dog.read_text()






# 10-9. Silent Cats and Dogs




# 10-10. Common Words
