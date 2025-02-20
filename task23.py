# Demonstrate the use of try, except, and finally block statements

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        return None
    finally:
        print("Execution of the try-except block is complete.")
    return result

# Test the function with different inputs
print(divide_numbers(10, 2))  # Valid input
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, "a"))  # Invalid input type
