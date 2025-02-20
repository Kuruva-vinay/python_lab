# Create a tuple and perform various operations

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Add items to the tuple (tuples are immutable, so we create a new tuple)
new_tuple = my_tuple + (6, 7)
print("After adding items:", new_tuple)

# Find the length of the tuple
print("Length of the tuple:", len(my_tuple))

# Check if an item exists in the tuple
print("3 in my_tuple:", 3 in my_tuple)
print("6 in my_tuple:", 6 in my_tuple)

# Access items in the tuple
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])
print("Slice of tuple:", my_tuple[1:4])
