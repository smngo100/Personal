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
# Use DOT NOTATION to access the car's odometer_reading attribute, and set its value directly 
class Car:
    --snip--
  
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


##### Modifying an Attribute's Value Through a Method #####
class Car:
    --snip--

    def update_odometer(self, mileage):
        #"""Set the odometer reading to the given value."""
        self.odometer_reading = mileage
      
my_new_car.update_odometer(23)
my_new_car.read_odometer()


##### Incrementing an Attribute's Value Through a Method #####
class Car:
    --snip--

  def update_odometer(self, mileage):
    --snip--
  
  def increment_odometer(self, miles):
    #"""Add the given amount to the odometer reading."""
    self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
