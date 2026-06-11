import numpy as np

np.random.seed(42)  
arr = np.random.randint(1, 100, size=10)

print("Original Array:")
print(arr)

normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("\nNormalized Array:")
print(normalized_arr)