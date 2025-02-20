# Define a module and import a specific function from that module into another program

# Define a module named `my_module.py`
def greet(name):
    return f"Hello, {name}!"

# Save the above code in a file named `my_module.py`

# Import the `greet` function from `my_module` into another program
from my_module import greet

# Use the imported function
name = "Alice"
print(greet(name))
