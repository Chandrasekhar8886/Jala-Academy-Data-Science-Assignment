import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

U, S, VT = np.linalg.svd(A)

Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)

A_reconstructed = U @ Sigma @ VT

print("Original Matrix:")
print(A)

print("\nU Matrix:")
print(U)

print("\nSingular Values:")
print(S)

print("\nVT Matrix:")
print(VT)

print("\nReconstructed Matrix:")
print(A_reconstructed)