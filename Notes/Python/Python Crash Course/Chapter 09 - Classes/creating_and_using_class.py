"""
Object-oriented programming (OOP) is one of the most effective approaches to writing software.
* You write classes that represent real-world things and situations
* You create objects based on these classes 
* When you write a class, you define the general behavior that a whole category of objects can have
"""

##### Definitions #####
# Instantiation: Making an object from a class, and you work with instances of a class
# Instance: An individual object created from a class
# Method: A function that's part of a class
# Attribute: Variables that are accessible through instances


##### Notes #####
# By convention, capitalized names refer to classes in Python
# No parentheses in the class definition


##### The __init__() Method ##### 
# Special method that Python runs automatically whenever we create a new instance based on the class
# Any variable prefixed with self is available to every method in the class


##### Making an Instance from a Class #####
# Make an instance from the Dog class and assign it to the variable my_dog
my_dog = Dog('Willie', 6)


##### Accessing Attributes #####
# To access the attributes of an instance, you use DOT NOTATION. 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # So attribute name is name


variable_name.attribute_name
my_dog.name

##### Calling Methods #####
# Use dot notation to call any method 
# Variable then call method from the class 
# sit() is a method that's part of class Dog 
my_dog.sit()
my_dog.roll_over()
