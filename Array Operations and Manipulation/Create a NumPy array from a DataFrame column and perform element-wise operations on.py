import pandas as pd
import numpy as np

data = {
    'Marks': [70, 80, 90, 60, 85]
}

df = pd.DataFrame(data)

marks_array = df['Marks'].to_numpy()

print("Original Array:")
print(marks_array)

add_10 = marks_array + 10
multiply_2 = marks_array * 2
square = marks_array ** 2

print("\nAdd 10:")
print(add_10)

print("\nMultiply by 2:")
print(multiply_2)

print("\nSquare of Elements:")
print(square)