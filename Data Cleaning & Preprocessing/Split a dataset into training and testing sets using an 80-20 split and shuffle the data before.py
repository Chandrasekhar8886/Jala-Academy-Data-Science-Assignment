import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    'Age': [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Salary': [30000, 35000, 40000, 45000, 50000,
               55000, 60000, 65000, 70000, 75000],
    'Purchased': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

X = df[['Age', 'Salary']]
y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    shuffle=True,
    random_state=42
)

print("Training Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)