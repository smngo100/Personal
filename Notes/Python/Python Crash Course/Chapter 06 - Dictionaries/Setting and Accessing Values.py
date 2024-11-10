# Accessing Values
"""
- When you use a key within square brackets with a dictionary, it retrieves the value associated with that key
- Accessing a Value for a Key (Right Side of Assignment or in an Expression) 
- When you use brackets on the right side of an assignment or within an expression, you are accessing the value associated with a specific key in the dictionary
"""

responses = {'Alice': 'Hello, world!'}  # Existing dictionary
name = "Alice"  # Define a key

# Accessing the value for the key "Alice"
response = responses[name]  # This retrieves 'Hello, world!' and assigns it to `response`
print(response)  # Output: Hello, world!


# Setting Values 
""" 
- Setting a Value for a Key (Left Side of Assignment) 
- When you use brackets on the left side of an assignment, you are setting or updating the value associated with a specific key in the dictionary
- When you use a key within square brackets and assign a value to it, it either updates an existing key or adds a new key-value pair to the dictionary
"""

nses = {}  # Create an empty dictionary
name = "Alice"  # Define a key
response = "Hello, world!"  # Define a value

# Setting the value for the key "Alice"
responses[name] = response  # Now, responses = {'Alice': 'Hello, world!'}
# responses[name] = response sets the value for the key "Alice" to "Hello, world!".


######################################## SUMMARY ########################################
"""

- Setting a value: 
  response[key] = value 
  * This assigns value to the dictionary for the given key.

- Accessing a value: 
  value = response[key]
  * This retrieves the value for the given key from the dictionary.
  
"""






