# 9-6. Ice Cream Stand
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is now open.")


# IceCreamStand class inherits from Restaurant class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):    # * enables us to pass an arbitrary number of arguments
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors  # new attribute that stores a list of ice cream flavors

    def display_flavors(self):
        print(f"Ice cream flavors: {self.flavors}.")

# Make an instance of the IceCreamStand class and assign it to the variable ice_cream
ice_cream = IceCreamStand('Baskin Robins', 'ice cream', 'vanilla', 'chocolate', 'strawberry')
ice_cream.display_flavors()


# 9-7. Admin
class Users:
    def __init__(self, first_name, last_name, fav_color, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_color = fav_color
        self.hobby = hobby

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}"
              f"\nFavorite Color: {self.fav_color.title()}"
              f"\nHobby: {self.hobby.title()}")

    def greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}!\n")


# Admin class inherits from Users class
class Admin(Users):
    def __init__(self, first_name, last_name, fav_color, hobby, *privileges):
        super().__init__(first_name, last_name, fav_color, hobby)
        self.privileges = privileges    # new attribute privileges that stores a list of strings 

# Make an instance of the Admin class and assign it to the variable _admin
_admin = Admin('blueberry', 'muffin', 'blue', 'baking', 'can add post', 'can delete post', 'can ban user')


# 9-8. Privileges
# Separate Privileges class
class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges    # stores a list of strings

    # Moved the show_privileges method to the Privileges class 
    def show_privileges(self):  
        print(f"Administrator's set of privileges: {self.privileges}.")

class Admin(Users):
    def __init__(self, first_name, last_name, fav_color, hobby, *admin_privileges):
        super().__init__(first_name, last_name, fav_color, hobby)
        self.privileges = Privileges(*admin_privileges)

# Make a new instance of the Admin class and assign it to the variable _admin
_admin = Admin('blueberry', 'muffin', 'blue', 'baking', 'can add post', 'can delete post', 'can ban user')
_admin.privileges.show_privileges()


# 9-9. Battery Upgrade
# Use final version of electric_car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    # New method that checks the battery size and sets the capacity to 65 if it isn't already
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
