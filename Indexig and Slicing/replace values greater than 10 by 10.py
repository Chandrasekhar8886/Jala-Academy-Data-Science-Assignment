import numpy as np

arr = np.array([5, 12, 8, 15, 20, 7, 10, 18, 3])

arr[arr > 10] = 10

print("Modified Array:")
print(arr)