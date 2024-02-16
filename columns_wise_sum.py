# Define a 3 by 3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Get the number of columns in the matrix
num_columns = len(matrix[0])

# Initialize an empty list to store column-wise sums
column_sums = [0] * num_columns

# Iterate over each row and column to calculate column-wise sums
for row in matrix:
    for j in range(num_columns):
        column_sums[j] += row[j]

# Print the column-wise sums
print("Column-wise Sums without Functions:", column_sums)

# output will be like
 [11 15 17]

# this the way of process

that is the code we have
