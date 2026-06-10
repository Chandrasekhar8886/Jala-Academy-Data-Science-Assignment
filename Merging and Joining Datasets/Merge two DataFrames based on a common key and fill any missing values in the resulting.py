import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

employees = pd.read_csv(os.path.join(current_dir, "employees.csv"))
salaries = pd.read_csv(os.path.join(current_dir, "salaries.csv"))

print("Employees DataFrame:")
print(employees)

print("\nSalaries DataFrame:")
print(salaries)

merged_df = pd.merge(employees, salaries, on="EmployeeID", how="outer")

print("\nMerged DataFrame:")
print(merged_df)

merged_df["Name"] = merged_df["Name"].fillna("Unknown")
merged_df["Salary"] = merged_df["Salary"].fillna(0)

print("\nMerged DataFrame after filling missing values:")
print(merged_df)