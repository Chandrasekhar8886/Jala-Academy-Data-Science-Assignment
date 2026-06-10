import numpy as np

arr1 = np.random.randint(1, 11, size=(2, 3))
arr2 = np.random.randint(1, 11, size=(2, 3))

addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nAddition:")
print(addition)

print("\nSubtraction:")
print(subtraction)

print("\nMultiplication:")
print(multiplication)

print("\nDivision:")
print(division)