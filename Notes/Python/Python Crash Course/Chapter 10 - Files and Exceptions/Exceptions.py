##### Exceptions #####
# Exceptions: Special objects used to manage errors that arise during a program's execution.
    # Handled with try-except blocks
# Try-except block asks Python to do something, but it also tells Python what to do if an exception is raised.

##### Using try-except Blocks #####
# When you think an error may occur, you can write a try-except block to handle the exception that might be raised.
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print()


##### The else Block #####
# Any code that depends on the try block executing successfully goes in the else block
# If the division operation is successful, we use the else block to print the result
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
# The only code that should go in a try block is code that might cause an expcetion to be raised.


##### Handling the FileNotFoundError Exception ##### 

