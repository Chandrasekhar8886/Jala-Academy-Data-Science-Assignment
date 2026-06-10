import numpy as np

arr = np.random.randint(1, 101, size=100)

even_sum = np.sum(arr[arr % 2 == 0])

print("Array:")
print(arr)

print("\nSum of all even numbers:")
print(even_sum)