##### Unit Tests and Test Cases ##### 
# A 'UNIT TEST' verifies that one specific aspect of a function's behavior is correct. 
# A 'TEST CAST' is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of sutations you expect it to handle.
# A test case with 'FULL COVERAGE' includes a full range of unit tests covering all the possible ways you can use a function.


##### A Passing Test ##### 
# The name of a test file MUST start with test_
# because when we ask pytest to run the tests we've written, it will look for any file that begins with test_, and run all of the tests it finds in that file. 
# Test names should be longer and more descriptive than a typical function name.
# An assertion is a claim about a condition.


##### Runnning a Test ##### 
# To let pytest run the test file, open a termal window and navigate to the folder that contains the test file.
# In the terminal window, enter the command pytest


##### A Failing Test ##### 
# F next to the file name means that one test failed. 
# An angle bracket ('<', '>') indicates the line of code that caused the test to fail. 
# E shows the actual error that caused the failure 


##### Responding to a Failed Test ##### 
# When a test fails, don't change the test. 
# If you do, your tests might pass, but any code that calls your function like the test does will suddent stop working. 
# Instead, fix the code that's causing the test to fail.
