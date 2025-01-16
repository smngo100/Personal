# 11-3. Employee

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
