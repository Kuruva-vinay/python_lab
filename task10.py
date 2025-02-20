# Find the remainder when the product of an array is divided by a given number n

def product_remainder(arr, n):
    product = 1
    for num in arr:
        product *= num
    remainder = product % n
    return remainder

# Input the array and the number n
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
n = int(input("Enter the number n: "))

# Calculate and display the remainder
result = product_remainder(arr, n)
print(f"The remainder when the product of the array is divided by {n} is: {result}")
