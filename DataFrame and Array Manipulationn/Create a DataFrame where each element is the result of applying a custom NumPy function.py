import numpy as np
import pandas as pd

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])

def custom_function(a, b):
    return a**2 + b**2

result = custom_function(arr1, arr2)

df = pd.DataFrame(result,
                  columns=['Col1', 'Col2', 'Col3'])

print(df)