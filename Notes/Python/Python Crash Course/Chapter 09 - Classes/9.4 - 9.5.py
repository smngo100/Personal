# 9-4. Number Served
# Start with program from exercise 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # add default value of 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is now open.")

    # Create new method that displays the number of customers the restaurant has served
    def customers_served(self):
        print(f"{self.restaurant_name.title()} has served {self.number_served} customers.")

    # Create new method that sets the number of customers that have been served
    def set_number_served(self, served):
        self.number_served = served

    # Create new method that increments the number of customers who've been served
    def increment_number_served(self, served):
        self.number_served += served


##### Modifying an Attribute's Value Directly #####
restaurant = Restaurant('in-n-out', 'burgers')
restaurant.number_served = 105  # the number of customers the restaurant has served
restaurant.customers_served()   # call method to display statement


##### Modifying an Attribute's Value through a Method #####
restaurant.set_number_served(120)   # pass new value to method
restaurant.customers_served()       # call method to display statement


##### Incrementing an Attribute's Value Through a Method #####
restaurant.set_number_served(150)           # set number of customers served to 150 customers
restaurant.customers_served()
restaurant.increment_number_served(130)     # add 100 customers
restaurant.customers_served()


# 9-5. Login Attempts
# Start with program from exercise 9-3
class Users:
    def __init__(self, first_name, last_name, fav_color, hobby, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_color = fav_color
        self.hobby = hobby
        self.login_attempts = login_attempts    # new attribute

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}"
              f"\nFavorite Color: {self.fav_color.title()}"
              f"\nHobby: {self.hobby.title()}")

    def greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

# Make an instance from the Users class and assign it to the variable user
user = Users('mochiz', 'cheese', 'blue', 'gaming', 5)

# Call increment_login_attempts several times
print("\nLogin attempts: ", end = "")
count1 = user.increment_login_attempts()
count2 = user.increment_login_attempts()
count3 = user.increment_login_attempts()
print(count1, end = " ")
print(count2, end = " ")
print(count3, end = " ")

print(f"\nUser login attempts: {user.login_attempts}")

# Reset login_attempts
print(f"\nReset login attempts: ", end = "")
reset = user.reset_login_attempts()
print(reset)
