import numpy as np

A = np.array([
    [3, 4],
    [5, 2]
])

B = np.array([7, 8])

solution = np.linalg.solve(A, B)

x, y = solution

print("x =", x)
print("y =", y)