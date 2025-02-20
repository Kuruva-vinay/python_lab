# Find numbers that are divisible by 7 and are multiples of 5 between 1500 and 2700 (both inclusive)

def find_divisible_numbers():
    result = []
    for num in range(1500, 2701):
        if num % 7 == 0 and num % 5 == 0:
            result.append(num)
    return result

# Display the result
divisible_numbers = find_divisible_numbers()
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700 (both inclusive):")
print(divisible_numbers)
