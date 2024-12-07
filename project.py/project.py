# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Data
file_path = 'https://raw.githubusercontent.com/Shihab25-0/Online-Streaming-Subscriptions/refs/heads/main/dataset.csv'  
data = pd.read_csv(file_path)

# 2. Explore the Data
print("Data Overview:")
print(data.info())
print("\nFirst 5 Rows:")
print(data.head())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDescriptive Statistics:")
print(data.describe())

# 3. Clean the Data
# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
# Drop rows with invalid dates (if any)
data = data.dropna(subset=['Date'])

# 4. Analyze the Data
# Example: Revenue by Product
revenue_by_product = data.groupby('Product')['Revenue'].sum()
print("\nRevenue by Product:")
print(revenue_by_product)

# Example: Average Price by Region
avg_price_by_region = data.groupby('Region')['Price'].mean()
print("\nAverage Price by Region:")
print(avg_price_by_region)

# 5. Visualize the Data
# Revenue by Product
plt.figure(figsize=(8, 5))
revenue_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.xticks(rotation=45)
plt.show()

# Quantity Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['Quantity'], bins=20, kde=True, color='green')
plt.title('Quantity Distribution')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

# 6. Draw Conclusions
print("\nConclusions:")
print("- The total revenue is highest for [Product Name] (from visual).")
print("- Customers in [Region Name] pay the highest average price.")

# Save cleaned data (optional)
data.to_csv('cleaned_data.csv', index=False)
