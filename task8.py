# Find the sum of squares of the digits of a given number

def sum_of_squares_of_digits(number):
    sum_squares = 0
    while number > 0:
        digit = number % 10
        sum_squares += digit ** 2
        number //= 10
    return sum_squares

# Input the number
number = int(input("Enter a number: "))

# Calculate and display the sum of squares of the digits
result = sum_of_squares_of_digits(number)
print(f"The sum of squares of the digits of {number} is: {result}")
