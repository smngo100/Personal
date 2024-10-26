# 3-8. Seeing the World
places = ["Italy", "France", "Spain", "Portugal", "Germany"]

print(f"Original order: {places}")
print(f"Sorted order: {sorted(places)}")
print(f"Still in original order after sorted: {places}")
print(f"Sorted in reverse order: {sorted(places, reverse = True)}")
print(f"Still in original order after sorted reverse: {places}")
places.reverse()
print(f"Reversed order: {places}")
places.reverse()
print(f"Reverse to change the order of the list again: {places}\n")

# 3-9. Dinner Guests
guest_list = ["Albert Einstein", "Vincent Van Gogh", "Bob Ross"]
print(f"I am inviting {len(guest_list)} people to the dinner\n")

# 3-10. Every Function
languages = ["Chinese", "Vietnamese", "French", "Spanish"]

############### Below uses every function introduced in Chapter 3 ###############
# Accessing Elements in a List
print(languages[1])

# Modifying Elements in a List
languages[3] = "Italian"
print(languages)

# Appending Elements to the End of a List
languages.append("English")
print(languages)

# Inserting Elements into a List
languages.insert(0, "Japanese")
print(languages)

# Removing an Item Using the del Statement
del languages[0]
print(languages)

# Removing an Item using the pop() Method
print(languages)
print(languages)
popped_language = languages.pop()
print(popped_language)

# Popping Items from Any Position in a List
languages.pop(2)
print(languages)

# Removing an Item by Value
languages.remove("Chinese")
print(languages)

# Index error
#print(languages[2])
