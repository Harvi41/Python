import numpy as np

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition
add = A + B

# Subtraction
sub = A - B

# Element-wise Multiplication
mul = A * B

# Matrix Multiplication
matmul = A @ B  # or np.dot(A, B)

# Transpose
transpose = A.T

# Inverse
inverse = np.linalg.inv(A)

# Determinant
det = np.linalg.det(A)

# Rank
rank = np.linalg.matrix_rank(A)

# Eigenvalues and Eigenvectors
eigvals, eigvecs = np.linalg.eig(A)

# Solve Ax = b
b = np.array([1, 2])
x = np.linalg.solve(A, b)
