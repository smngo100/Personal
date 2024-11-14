# 8-1. Message
def display_message():  # function definition
    print("I am learning about functions in this chapter.") # indented lines that follow the function definition make up the body of the funciton
display_message()   # function call: tells Python to execute the code in the function
# to call function, write name of function (as done here), followed by any necessary information in parentheses

# 8-2. Favorite Book
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")
favorite_book("Alice in Wonderland")
