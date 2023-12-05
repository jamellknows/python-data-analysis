import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate dummy e-commerce data
np.random.seed(42)

# Create a DataFrame with random data
num_entries = 1000
products = ['Laptop', 'Phone', 'Tablet', 'Headphones']
categories = ['Electronics', 'Electronics', 'Electronics', 'Accessories']
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
customer_ids = np.random.randint(1001, 1101, size=num_entries)
product_ids = np.random.choice(range(1, 5), size=num_entries)
purchase_amounts = np.random.uniform(50, 1000, size=num_entries)

df = pd.DataFrame({
    'Date': np.random.choice(dates, size=num_entries),
    'CustomerID': customer_ids,
    'ProductID': product_ids,
    'Product': [products[i - 1] for i in product_ids],
    'Category': [categories[i - 1] for i in product_ids],
    'Amount': purchase_amounts
})

# Display the original data
print("Original DataFrame:")
print(df.head())
print("\n")

# Data Cleaning
print("Data Cleaning:")
# Remove duplicate entries
df = df.drop_duplicates()

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())
print("\n")

# Data Aggregation
print("Data Aggregation:")
# Total sales per product category
total_sales_per_category = df.groupby('Category')['Amount'].sum()
print(total_sales_per_category)
print("\n")

# Visualization
print("Data Visualization:")
# Plotting total sales per product category
plt.figure(figsize=(10, 6))
total_sales_per_category.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Product Category')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.show()
