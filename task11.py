# Implement the reversal algorithm for array rotation

def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, d):
    n = len(arr)
    if d == 0:
        return arr

    d = d % n  # Handle cases where d > n

    # Reverse the first part
    reverse_array(arr, 0, d - 1)
    # Reverse the second part
    reverse_array(arr, d, n - 1)
    # Reverse the whole array
    reverse_array(arr, 0, n - 1)

    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotated_arr = rotate_array(arr, d)
print("Rotated array:", rotated_arr)
