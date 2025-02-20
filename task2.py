# Create a list and perform various methods

# Create a list
my_list = [1, 2, 3, 4, 5]

# Insert an element at a specific position
my_list.insert(2, 10)
print("After insert:", my_list)

# Remove an element from the list
my_list.remove(4)
print("After remove:", my_list)

# Append an element to the end of the list
my_list.append(6)
print("After append:", my_list)

# Get the length of the list
print("Length of the list:", len(my_list))

# Pop an element from the list
popped_element = my_list.pop()
print("After pop:", my_list)
print("Popped element:", popped_element)

# Clear the list
my_list.clear()
print("After clear:", my_list)
