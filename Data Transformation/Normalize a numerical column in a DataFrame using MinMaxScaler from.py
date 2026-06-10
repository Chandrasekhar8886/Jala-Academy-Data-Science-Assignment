import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "student_scores.csv")

print("CSV Path:", csv_path)
print("File Exists:", os.path.exists(csv_path))
print("Files in Current Folder:")
print(os.listdir(os.path.dirname(os.path.abspath(__file__))))

df = pd.read_csv(csv_path)

print("Original Data:")
print(df)

scaler = MinMaxScaler()

df["Normalized_Score"] = scaler.fit_transform(df[["Score"]])

print("\nData after Min-Max Normalization:")
print(df)