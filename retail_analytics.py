import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Dataset
file_path = 'retail_data.csv'
df = pd.read_csv(file_path)

print("========== RETAIL DATA ==========")
print(df.head())

# Basic Information
print("========== DATASET INFO ==========")
print(df.info())

# Missing Values
print("========== MISSING VALUES ==========")
print(df.isnull().sum())

# Total Sales KPI
print("========== TOTAL SALES ==========")
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Total Profit KPI
print("========== TOTAL PROFIT ==========")
total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

# Best Selling Product
print("========== TOP PRODUCT ==========")
product_sales = df.groupby('Product')['Sales'].sum()
top_product = product_sales.idxmax()
print("Top Product:", top_product)
# Region Wise Analysis
print("========== REGION SALES ==========")
region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

# Category Wise Analysis
print("========== CATEGORY SALES ==========")
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)

# Customer Purchase Analysis
print("========== TOP CUSTOMER ==========")
customer_sales = df.groupby('Customer_Name')['Sales'].sum()
top_customer = customer_sales.idxmax()
print("Top Customer:", top_customer)
# Average Profit
print("========== AVERAGE PROFIT ==========")
print(df['Profit'].mean())

# Create Charts Folder
if not os.path.exists('charts'):
    os.makedirs('charts')

# Chart 1: Region Sales
plt.figure(figsize=(7,5))
region_sales.plot(kind='bar')
plt.title('Region Wise Sales')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('charts/region_sales.png')
plt.close()
# Chart 2: Category Distribution
plt.figure(figsize=(6,6))
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Category Wise Sales Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('charts/category_distribution.png')
plt.close()

# Chart 3: Product Sales
plt.figure(figsize=(8,5))
product_sales.plot(kind='line', marker='o')
plt.title('Product Performance')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/product_performance.png')
plt.close()
# Export Excel Report
with pd.ExcelWriter('sales_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Raw_Data', index=False)
    region_sales.to_excel(writer, sheet_name='Region_Sales')
    category_sales.to_excel(writer, sheet_name='Category_Sales')
    product_sales.to_excel(writer, sheet_name='Product_Sales')

print("Excel report generated successfully!")
print("Charts saved inside charts folder!")

print("========== PROJECT COMPLETED ==========")

