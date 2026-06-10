import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

customers = pd.read_csv(os.path.join(current_dir, "customers.csv"))
orders = pd.read_csv(os.path.join(current_dir, "orders.csv"))

print("Customers DataFrame:")
print(customers)

print("\nOrders DataFrame:")
print(orders)

result = pd.merge(
    customers,
    orders,
    left_on="CustomerID",
    right_on="CustID",
    how="left"
)

print("\nAfter Left Join:")
print(result)

result["OrderAmount"] = result["OrderAmount"].fillna(0)

print("\nAfter Handling Missing Values:")
print(result)