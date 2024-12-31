# 10-6. Addition
"""Prompts user for two numbers and prints their sum."""

# Not using while loop
try:
    num1 = int(input("\nEnter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
except ValueError:
    print("You must enter a number.")
else:
    print(sum)
    

# Using while loop
while True:

    num1 = input("\nEnter the first number: ")
    if num1 == 'q':
        break
    try:
        num1 = int(num1)
    except ValueError:
        print("You must enter a number.")


    num2 = input("Enter the second number: ")
    if num2 == 'q':
        break
    try:
        num2 = int(num2)
    except ValueError:
        print("You must enter a number.")
    else:
        result = num1 + num2
        print(result)





# 10-7. Addition Calculator




# 10-8. Cats and Dogs



# 10-9. Silent Cats and Dogs




# 10-10. Common Words
