# Inheritance: When one class inherits from another, it takes on the attributes and methods of the first class.
# Parent class: The original class
# Child class: The new class that can inherit any or all of the attributes and methods of its parent class,
# but it's also free to define new attributes and methods of its own.


##### The __init__() Method for a Child Class #####
# When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
    # I think that's not true because you can just import the parent class into the module containing the child class.
# The name of the parent class must be included in the parentheses in the definition of a child class.
    # class child(Parent)
    # child class inherits from Parent class

# super() function is a special function that allows you to call a method from the parent class.
# The name super comes from a convention of calling the parent class a superclass and the child class a subclass.
super().__init__(parameter(s))
# *NOTE*: When calling super() we don't have self, it's just the parent class parameters

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class child(Parent):
    def __init(self, name, age, school):
        super().__init__(name, age) # Passing parent class parameters
        self.school = school        # Additional parameter specific to child class


##### Defining Attributes and Methods for the Child Class #####
# To define an attribute specific to the child class just add the attribute below the super.__init__(parameter)
class Car:
  --snip--

class ElectricCar(Car): # class ElectricCar inherits from the class Car
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery_size = 40  # Attribute specific to the child class


##### Overriding Methods from the Parent Class #####
# You can override any method from the parent class that doesn't fit what you're trying to model with the child class.
# To do this, you define a method in the child class with the same name as the method you want to override in the parent class.
# Python will disregard the parent class method and only pay attention to the method you define in the child class.
class ElectricCar(Car):
  --snip--

  def fill_gas_tank(self):
    print("This car doesn't have a gas tank!")
# Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore this method in Car and run this code instead.
# When you use inheritance, you can make your child class retain what you need and override anything you don't need from the parent class.


##### Instances as Attributes #####
# Composition: Break larger class into smaller classes that work together
# Define a new class that doesn't inherit from any other class
class Battery():
  def __init__(self, battery_size=40):
    self.battery_size = battery_size

  def describe_battery(self):
    print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery = Battery()  # battery attribute


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
# When we want to describe the battery, we work through the car's battery attribute

# So, basically
variable.attribute_name.method_name()
