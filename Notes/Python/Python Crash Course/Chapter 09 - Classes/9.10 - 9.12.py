# 9-10. Imported Restaurant 
import restaurant

_restaurant = restaurant.Restaurant('in-n-out', 'burgers')
_restaurant.describe_restaurant()
_restaurant.open_restaurant()


# 9-11. Imported Admin 
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

class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges    # stores a list of strings

    # Moved the show_privileges method to the Privileges class
    def show_privileges(self):
        print(f"Administrator's set of privileges: {self.privileges}.")

# Make a new instance of the Admin class and assign it to the variable _admin
_admin = Admin('blueberry', 'muffin', 'blue', 'baking', 'can add post', 'can delete post', 'can ban user')





# 9-12. Multiple Modules 





