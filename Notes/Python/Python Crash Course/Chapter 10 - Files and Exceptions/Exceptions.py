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
    if first_number == 'quit':
        break
    second_number = input("Second number: ")
    if second_number == 'quit':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
# The only code that should go in a try block is code that might cause an expcetion to be raised.


##### Handling the FileNotFoundError Exception ##### 
"""
It's often best to start at the very end of the traceback. On the last last, we see the exception that was raised.
This is important because it tells us what kind of exception to use in the except block that we'll write.
The beginning of the tracebook shows where the error occured. The next line shows the line of code that caused the error. 
To handle the error that's being raised, the try block will begin with the line that was identified as problematic in the traceback.
* The try block code is basically the line of code that caused the error. 
"""

# Example 
from path import Path 
path = Path('alice.txt') 
contents = path.read_text(encoding='utf-8) 
# We'd get a traceback error of the line contents . . . because alice.txt isn't in our path. 
# We can handle the error weith a try block 
try: 
    contents = path.read_text(encoding='utf-8) 
except FileNotFoundError:                         
    print(f"Sorry, the file {path} does not exist.")


##### Analyzing Text ##### 
# string method split() default splits a string wherever it finds any whitespace 
from pathlib import Path
path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

##### Working with Multiple Files ##### 
from pathlib import Path
def count_words(filename):
    --snip--
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
        'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)


##### Failing Silently ##### 
# To make a program fail silently, you write a try block as usualy, but you explictly tell Python to do nothing in the except block. 
# Python has a pass statement that tells it to do nothing in a block 
try: 
    --snip-- 
except FileNotFoundError: 
    pass
else: 
    --snip--


