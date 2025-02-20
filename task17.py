# Find the nth multiple of a given number in the Fibonacci series

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def nth_multiple_in_fibonacci(n, multiple):
    count = 0
    i = 1
    while True:
        fib_num = fibonacci(i)
        if fib_num % multiple == 0:
            count += 1
            if count == n:
                return fib_num
        i += 1

# Input the value of n and the multiple
n = int(input("Enter the value of n: "))
multiple = int(input("Enter the multiple: "))

# Calculate and display the nth multiple of the given number in the Fibonacci series
result = nth_multiple_in_fibonacci(n, multiple)
print(f"The {n}th multiple of {multiple} in the Fibonacci series is: {result}")
