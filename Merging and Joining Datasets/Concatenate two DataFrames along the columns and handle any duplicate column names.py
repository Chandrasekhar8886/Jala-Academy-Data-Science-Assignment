import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

students = pd.read_csv(os.path.join(current_dir, "students.csv"))
marks = pd.read_csv(os.path.join(current_dir, "marks.csv"))

print("Students DataFrame:")
print(students)

print("\nMarks DataFrame:")
print(marks)

result = pd.concat([students, marks], axis=1)

print("\nAfter Concatenation:")
print(result)

result.columns = [
    "Student_ID",
    "Name",
    "Marks_ID",
    "Marks"
]

print("\nAfter Renaming Duplicate Columns:")
print(result)