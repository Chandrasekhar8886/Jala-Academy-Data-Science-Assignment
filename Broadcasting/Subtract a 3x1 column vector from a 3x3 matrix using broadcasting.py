import numpy as np

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

column_vector = np.array([[1],
                          [2],
                          [3]])

result = matrix - column_vector

print("3x3 Matrix:")
print(matrix)

print("\n3x1 Column Vector:")
print(column_vector)

print("\nResult:")
print(result)