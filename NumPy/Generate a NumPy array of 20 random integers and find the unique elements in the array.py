import numpy as np

np.random.seed(42) 
arr = np.random.randint(1, 11, size=20)

print("Original Array:")
print(arr)

unique_elements = np.unique(arr)

print("\nUnique Elements:")
print(unique_elements)