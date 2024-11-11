"""
Attributes:
Definition: 
  Attributes are variables that belong to an object (an instance of a class). They represent the characteristics or properties of that object.
Access: 
  Attributes can be accessed using the dot notation (object.attribute).
Types:
  Instance attributes: These attributes are unique to each instance of a class. They are defined within the class's methods, typically within the __init__ method, and are accessed using the self keyword.
  Class attributes: These attributes are shared among all instances of a class. They are defined directly within the class body, outside of any method, and can be accessed using the class name or an instance of the class. 
 
State:
Definition: 
  The state of an object refers to the current values of its attributes. It represents the condition or situation of the object at a particular point in time.
Change: 
  An object's state can change over time as its attributes are modified.
"""

# Example 
class Car:
    wheels = 4  # Class attribute

    def __init__(self, color, make):
        self.color = color  # Instance attribute
        self.make = make    # Instance attribute

    def repaint(self, new_color):
        self.color = new_color  # Changing the state of the object

"""
In this example:
wheels is a class attribute representing a property shared by all cars.
color and make are instance attributes, unique to each car object.
The repaint method modifies the color attribute, changing the state of the car object.

Key Differences:
Scope:
  Attributes are the variables themselves, while state is the collective value of those variables at a given time.
Persistence:
  Attributes are a permanent part of an object's structure, while state can change dynamically throughout the object's lifetime.
Access:
  Attributes are accessed directly, while state may be inferred from the values of multiple attributes.
"""
