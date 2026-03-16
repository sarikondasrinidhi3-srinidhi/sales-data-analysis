import pandas as pd

# Read the CSV file
data = pd.read_csv("sales.csv")

# Show the data
print("Sales Data:")
print(data)

# Calculate total sales
data["Total"] = data["Quantity"] * data["Price"]

# Group by product and calculate total sales
total_sales = data.groupby("Product")["Total"].sum()

print("\nTotal sales per product:")
print(total_sales)


import matplotlib.pyplot as plt

total_sales.plot(kind="bar")

plt.title("Total Sales per Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.show()