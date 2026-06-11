import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])

def square(x):
    return x ** 2

result = s.apply(square)

print("Original Series:")
print(s)

print("\nModified Series:")
print(result)