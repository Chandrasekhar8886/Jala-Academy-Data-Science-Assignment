import numpy as np
import pandas as pd

A = np.array([
    [2, 1],
    [1, -1]
])

B = np.array([5, 1])

solution = np.linalg.solve(A, B)

df = pd.DataFrame({
    'Variable': ['x', 'y'],
    'Value': solution
})

print(df)