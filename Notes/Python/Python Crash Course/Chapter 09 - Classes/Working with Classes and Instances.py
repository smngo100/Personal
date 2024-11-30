##### Setting a Default Value for an Attribute #####
class Car:

def __init__(self, make, model, year):
  """Initialize attributes to describe a car."""
  self.make = make
  self.model = model
  self.year = year
  self.odometer_reading = 0  # default value


---------------------------------------- Modifying Attribute Values ----------------------------------------
# Can change an attribute's value in 3 ways: 
# 1) Change the value directly through an instance
# 2) Set the value through a method 
# 3) Increment the value (add a certain amount to it) through a method 


##### Modifying an Attribute's Value Directly #####




