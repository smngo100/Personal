# 9-1. Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is open.")

restaurant = Restaurant('pizza hut', 'pizza')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2. Three Restaurants
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is open.")

restaurant1 = Restaurant('del taco', 'tacos')
restaurant2 = Restaurant('in-n-out', 'burgers')
restaurant3 = Restaurant('kfc', 'chicken')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# 9-3. Users
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old.")

    def greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}.")

user1 = User('mochiz', 'cheese', 19)
user2 = User('blueberry', 'muffin', 14)
user3 = User('cream', 'puff', 10)

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
