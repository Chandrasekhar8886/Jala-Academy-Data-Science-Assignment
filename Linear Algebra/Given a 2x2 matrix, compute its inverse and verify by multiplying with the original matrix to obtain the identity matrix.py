import numpy as np

A = np.array([[4, 7],
              [2, 6]])

A_inv = np.linalg.inv(A)

identity = np.dot(A, A_inv)

print("Original Matrix:")
print(A)

print("\nInverse Matrix:")
print(A_inv)

print("\nA × A_inv:")
print(identity)