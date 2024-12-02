# Inheritance: When one class inherits from another, it takes on the attributes and methods of the first class.
# Parent class: The original class 
# Child class: The new class that can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes and methods of its own.


##### The __init__() Method for a Child Class #####
# When you create a child class, the parent class must be part of the current file and must appear before the child class in the file. 
# The name of the parent class must be included in the parentheses in the definition of a child class. 

# super() function is a special function that allows you to call a method from the parent class
# The name super comes from a convention of calling the parent class a superclass and the child class a subclass
super().__init__(parameter)


##### Defining Attributes and Methods for the Child Class #####
# To define an attribute specific to the child class just add the attribute below the super.__init__(parameter) 
class Car:
  -- snip -- 

class ElectricCar(Car): 
  def __init__(self, make, model, year): 
    super.__init__(make, model, year) 
    self.battery_size = 40  # attribute specific to the child class

