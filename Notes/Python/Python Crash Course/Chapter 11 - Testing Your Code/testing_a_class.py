# Assertion: A claim about a condition.

##### A Variety of Assertions ##### 
# Commonly Used Assertion Statements in Tests 
Assertion                       Claim 
assert a == b                   Assert that two values are equal.
assert a != b                   Assert that two values are not equal.
assert a                        Assert that a evaluates to True. 
assert not a                    Assert that a evaluates to False.
assert element in list          Assert that an element is in a list.
assert element not in list      Assert that an element is not in a list. 
# **NOTE**: These are just a few examples; anything that can be expressed as a conditional statement can be included in a test.


##### A Class to Test #####
# Testing a class is similar to testing a funciton, because much of the work involves testing the behavior of the methods in the class.


##### Testing the Class #####
# Write a test that verifies one aspect of the way the class behaves 


##### Using Fixtures #####
# Fixture: Helps set up a test environment 
# Decorator: A directive placed just before a function definition 
  # Python applies this directive to the function before it runs, to alter how the function code behaves.
# When you want to write a fixture, write a function that generates the resource that's used by multiple test functions. 
# Add the @pytest.fixture decorator to the new function, and add the name of this function as a parameter for each test function that uses this resource.
# Syntax: 
import pytest 

@pytest.fixture  # Add decorator before the function 
def function_name(): 
  --snip--
