import numpy as np

matrix = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

transposed = matrix.T

reshaped = transposed.reshape(3, 2)

print("Original Matrix:")
print(matrix)

print("\nTransposed Matrix:")
print(transposed)

print("\nReshaped Matrix (3x2):")
print(reshaped)