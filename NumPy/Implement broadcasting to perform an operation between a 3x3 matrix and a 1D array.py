import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr = np.array([10, 20, 30])

result = matrix + arr

print("Matrix:")
print(matrix)

print("\n1D Array:")
print(arr)

print("\nResult after Broadcasting:")
print(result)