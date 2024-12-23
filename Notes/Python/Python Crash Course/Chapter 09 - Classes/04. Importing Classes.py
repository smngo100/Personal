##### Importing a Single Class #####
# Module-level docstring briefly describes the contents of the module. You should write a docstring for each module you create.
# Example: (It's written above the class)
"""A class that can be used to represent a car."""

class Car:
  --snip--

# Import the Car class and create an instance from that class
# car is module name
# Car is class name
from car import Car
  my_new_car = Car('audi', 'a4', 2024)
  --snip--
# The import statement tells Python to open the car module and import the class Car. 
# Now we can use the Car class as if it were defined in this file.


##### Storing Multiple Classes IN a Module #####
# You can store as many classes as you need in a single module, although each class in a module should be related somehow.
class Car:
  --snip--

class Battery:
  --snip--

class ElectricCar(Car):
  --snip--

my_electric_car.py
from car import ElectricCar


##### Importing Multiple Classes FROM a Module #####
my_cars.py
from car import Car, ElectricCar
# You import multiple classes from a module by separating each class with a comma


##### Importing an Entire Module #####
import car
  my_new_car = car.Car('audi', 'a4', 2024)
  --snip--
# Syntax:
module_name.ClassName


##### Importing All Classes from a Module #####
# You can import every class from a module using the following syntax:
from module_name import *


##### Importing a Module into a Module #####
# Sometimes you'll want to spread out your classes over several modules to keep any one file from growing too large 
# and avoid storing unrelated classes in the same module.

electric_cary.py
from car import Car

class Battery:
  --snip--

class Electric(Car):
  --snip--
# The class ElectricCar needs access to its parent class Car, so we import Car directly into the module

car.py
class Car:
  --snip--

my_cars.py # aka main.py
from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())


##### Using Aliases #####

# Give class an alias
from electric_car import ElectricCar as EC
my_leaf = EC('nissan', 'leaf, 2024)

# Give module an alias
# Now you can use this module alias with the full class name
import electric_car as ec
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
