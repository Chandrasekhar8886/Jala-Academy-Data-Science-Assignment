import numpy as np

def matrix_inverse(matrix):
    """
    Returns the inverse of a square matrix.
    """
    return np.linalg.inv(matrix)

A = np.array([
    [4, 7],
    [2, 6]
])

inverse_A = matrix_inverse(A)

print("Original Matrix:")
print(A)

print("\nInverse Matrix:")
print(inverse_A)