# 9-1. Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is now open.")

# Instance
restaurant = Restaurant('in-n-out', 'burgers')

# Print the two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()


# 9-2. Three Restaurants
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is now open.")

# Three different instances
r1 = Restaurant('taco bell', 'tacos')
r2 = Restaurant('dominos', 'pizza')
r3 = Restaurant('the habit', 'burgers')

# Call describe_restaurant() for each instance
r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()
print()


# 9-3. Users
class Users:
    def __init__(self, first_name, last_name, fav_color, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_color = fav_color
        self.hobby = hobby

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}"
              f"\nFavorite Color: {self.fav_color}"
              f"\nHobby: {self.hobby}")

    def greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}!\n")

# Several instances representing different users 
user1 = Users('mochiz', 'cheese', 'blue', 'gaming')
user2 = Users('blueberry', 'muffin', 'lavender', 'baking')
user3 = Users('spaghetti', 'meatball', 'red', 'cooking')

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
