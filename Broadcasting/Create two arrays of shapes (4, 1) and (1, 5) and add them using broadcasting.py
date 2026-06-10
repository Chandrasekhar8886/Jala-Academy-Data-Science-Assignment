import numpy as np

a = np.array([[1],
              [2],
              [3],
              [4]])      

b = np.array([[10, 20, 30, 40, 50]])  

result = a + b

print("Array A:")
print(a)
print("Shape:", a.shape)

print("\nArray B:")
print(b)
print("Shape:", b.shape)

print("\nResult:")
print(result)
print("Shape:", result.shape)