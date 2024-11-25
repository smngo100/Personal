# Module: a file ending in .py that contaisn the code you wan tto import into your program

"""
# Importing an Entire Module 

  import module_name

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Each function in the module is available through the following syntax:

  module_name.function_name() 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You can also import a SPECIFIC FUNCTION from a module: 

  from module_name import function_name
  
* Note: when you import just the function you're going to use, with this syntax, you don't need to use the dot notation when you call a function because we've explicitly imported the function in the import statement, we can call it by name when we use the function

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You can import as many functions as you want from a module by separating each function's name with a comma: 
 
  from module_name import function_0, function_1, function_2

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Using 'as' to Give a FUNCTION an Alias 
If the name of a function you're importing might conflict with an existing name in your program, or if the function name is long, you can use a short, unique alias - an alternate name simialr to a nickname for the function.

  from module_name import function_name as fn 
  
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Using 'as' to Give a MODULE an Alias

  import module_name as mn

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Importing all Functions in a Module

  from module_name import * 

"""
