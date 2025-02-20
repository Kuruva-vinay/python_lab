# Find the sum of the first n even numbers

def sum_of_even_numbers(n):
    sum_even = 0
    for i in range(1, n + 1):
        sum_even += 2 * i
    return sum_even

# Input the value of n
n = int(input("Enter the value of n: "))

# Calculate and display the sum of the first n even numbers
result = sum_of_even_numbers(n)
print(f"The sum of the first {n} even numbers is: {result}")
