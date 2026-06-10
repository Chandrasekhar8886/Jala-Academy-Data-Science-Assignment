import numpy as np

arr = np.random.randint(0, 11, size=(3, 3))

total_sum = np.sum(arr)
mean_value = np.mean(arr)
std_dev = np.std(arr)

print("Array:")
print(arr)

print("\nSum:", total_sum)
print("Mean:", mean_value)
print("Standard Deviation:", std_dev)