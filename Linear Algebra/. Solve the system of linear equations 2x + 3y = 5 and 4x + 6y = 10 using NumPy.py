import numpy as np

A = np.array([[2, 3],
              [4, 6]])

B = np.array([5, 10])

try:
    solution = np.linalg.solve(A, B)
    print("Solution:", solution)
except np.linalg.LinAlgError as e:
    print("Error:", e)