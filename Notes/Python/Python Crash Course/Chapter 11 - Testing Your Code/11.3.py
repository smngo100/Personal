# 11-3. Employee
"""
Write a class called Employee. The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes. 
Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount.
Write a test file for Employee with two test functions, test_give_default_raise() and test_give_custom_raise(). 
Write your tests once without using a fixture, and make sure they both pass. 
Then write a fixture so you don’t have to create a new employee instance in each test function. Run the tests again, and make sure both tests still pass.
"""

##### Without using a fixture #####
# employee.py 
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5_000):
        self.annual_salary += raise_amount


# test_employee.py 
from employee import Employee

def test_give_default_raise():
    employee = Employee('Blueberry', 'Muffin', 60_000)
    employee.give_raise()
    assert employee.annual_salary == 65_000

def test_give_custom_raise():
    employee = Employee('Oatmeal', 'Raisin', 60_000)
    employee.give_raise(10_000)
    assert employee.annual_salary == 70_000


##### Using a fixture #####
# employee.py
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5_000):
        self.annual_salary += raise_amount

# test_employee.py 
from employee import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee('Blueberry', 'Muffin', 60_000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 65_000

def test_give_custom_raise(employee):
    employee.give_raise(10_000)
    assert employee.annual_salary == 70_000
