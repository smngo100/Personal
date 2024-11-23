# Accessing Elements in a list
* Access elemenet in a list by telling Python the position, or index of the item desired.
bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles[0]) # Output: trek 

######################################## Modifying, Adding, and Removing Elements ########################################

# Modifying Elements in a List 
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati' 
print(motorcycles) 
Output: ['ducati', 'yamaha', 'suzuki']

########## Adding Elements to a List ##########

# Appending Elements to the End of a List 
* append() method adds the new element to the end of the list.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') 
print(motorcycles) 
Output: ['honda', 'yamaha', 'suzuki', 'ducati']

# Inserting Elements into a List 
* Add a new element at any position in the list using the insert() method. Do so by specifying the index of the new element and the value of the new item.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') 
print(motorcycles) 
Output: ['ducati', 'honda', 'yamaha', 'suzuki']

########## Removing Elements in a List ##########

# Removing an Item Using the del Statement 
* Use del statement if you know the position of the item you want to remove from a list. 
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycle) 
Output: ['yamaha', 'suzuki']

# Removing an Item Using the pop() Method 
* pop() method removes the last item in a list, but it lets you work with that item after removing it. 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) 
popped_motorcycle = motorcycles.pop()
print(motorcycles) 
print(popped_motorcycle) 
Output: ['honda', 'yamaha', 'suzuki']
        ['honda', 'yamaha']
        suzuki

# Popping Items from Any Position in a List 
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an Item by Value
* Use the remove() method if you only know the value of the item you want to remove.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) 
motorcycles.remove('ducati')
print(motorcycles) 
Output: ['honda', 'yamaha', 'suzuki', 'ducati']
        ['honda', 'yamaha', 'suzuki']

######################################## Organizing a List ########################################

# Sorting a List Permanently with the sort() Method 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
Output: ['audi', 'bmw', 'subaru', 'toyota']

# Sorting a List Permanently with the sort() reverse Method 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)
Output: ['toyota', 'subaru', 'bmw', 'audi']

# Sorting a List Temporarily with the sorted() Function 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
Output: Here is the original list:
        ['bmw', 'audi', 'toyota', 'subaru']

        Here is the sorted list:
        ['audi', 'bmw', 'subaru', 'toyota']

        Here is the original list again:
        ['bmw', 'audi', 'toyota', 'subaru']

# Reversing a List Temporarily with the sorted() Function 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse = True))
Output: ['toyota', 'subaru', 'bmw', 'audi']

# Printing a List in Reverse Order 
* Use the reverse() method to reverse the original order of a list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
Output: ['bmw', 'audi', 'toyota', 'subaru']
        ['subaru', 'toyota', 'audi', 'bmw']
* Notice that reverse() doesn't sort backward alphabetically; it simply reverses the order of the list.
* reverse() method changes the order of a list permantely, but you can revert to the original order anytime by applying reverse() to the same list a second time.

# Find the Length of a List 
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
Output: 4
