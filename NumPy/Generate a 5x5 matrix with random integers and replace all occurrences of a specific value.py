import numpy as np

np.random.seed(42)  
matrix = np.random.randint(1, 10, size=(5, 5))

print("Original Matrix:")
print(matrix)

old_value = 5
new_value = 99

matrix[matrix == old_value] = new_value

print("\nModified Matrix:")
print(matrix)