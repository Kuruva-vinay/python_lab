# Print the transpose of a matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose

# Input matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Get the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the transposed matrix
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
