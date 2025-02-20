# Find the sum of squares of the first n natural numbers

def sum_of_squares(n):
    sum_squares = 0
    for i in range(1, n + 1):
        sum_squares += i ** 2
    return sum_squares

# Input the value of n
n = int(input("Enter the value of n: "))

# Calculate and display the sum of squares of the first n natural numbers
result = sum_of_squares(n)
print(f"The sum of squares of the first {n} natural numbers is: {result}")
