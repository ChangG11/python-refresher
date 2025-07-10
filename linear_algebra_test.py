import numpy as np

# Create vectors
vector_a_1 = np.array([1, 2, 3])
vector_b_1 = np.array([4, 5, 6])

# Create matrices
matrix_A_2 = np.array([[1, 2], [3, 4]])
matrix_B_2 = np.array([[5, 6], [7, 8]])


matrix_A_4 = np.array([[1,2,3],[4,5,6]])
matrix_B_4 = np.array([[7,8,9,10],[11,12,13,14],[15,16,17,18]])

# Addition of vectors
sum_vector = vector_a_1 + vector_b_1
print(f"Sum of vectors a and b: {sum_vector}")

# Subtraction of vectors
diff_vector = vector_a_1 - vector_b_1
print(f"Difference of vectors a and b: {diff_vector}")

# Dot product of vectors
dot_product = np.dot(vector_a_1, vector_b_1)
print(f"Dot product of vectors a and b: {dot_product}")

# Addition of matrices
sum_matrix = matrix_A_2 + matrix_B_2
print(f"Sum of matrices A and B: {sum_matrix}")

# Subtraction of matrices
diff_matrix = matrix_A_2 - matrix_B_2
print(f"Difference of matrices A and B: {diff_matrix}")

# Matrix multiplication
product_matrix = np.dot(matrix_A_4, matrix_B_4)
print(f"Product of matrices A and B: {product_matrix}")

# Transpose of a matrix
transpose_matrix = matrix_A_2.T
print(f"Transpose of matrix A: {transpose_matrix}")

# Magnitude of Vector
vector_a_5 = np.array([1,1,2])
magnitude = np.linalg.norm(vector_a_5)
print(f"Magnitude of vector a: {magnitude}")