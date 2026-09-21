import os
import pandas as pd
import matplotlib.pyplot as plt

# Create a folder for charts
os.makedirs("charts", exist_ok=True)

# Read the sales dataset
data = pd.read_csv("sales_data.csv")

print("\n===== BUSINESS DATA ANALYSIS & REPORTING SYSTEM =====")
print("\nFirst 5 records:")
print(data.head())

print("\nDataset information:")
print("Total records:", len(data))
print("Columns:", list(data.columns))

# Check and clean data
print("\nMissing values:")
print(data.isnull().sum())
data = data.drop_duplicates()

# Convert date and calculate sales
data["Date"] = pd.to_datetime(data["Date"])
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Basic analysis
total_sales = data["Total_Sales"].sum()
total_quantity = data["Quantity"].sum()
average_sale = data["Total_Sales"].mean()

product_sales = data.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
category_sales = data.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
region_sales = data.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
monthly_sales = data.groupby(data["Date"].dt.to_period("M"))["Total_Sales"].sum()

best_product = product_sales.idxmax()
best_region = region_sales.idxmax()

print("\n===== SALES SUMMARY =====")
print("Total sales: ₹", total_sales)
print("Total quantity sold:", total_quantity)
print("Average sale value: ₹", round(average_sale, 2))

print("\nProduct-wise sales:")
print(product_sales)

print("\nCategory-wise sales:")
print(category_sales)

print("\nRegion-wise sales:")
print(region_sales)

print("\nBest-selling product:", best_product)
print("Best-performing region:", best_region)

# Chart 1: Category sales
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.close()

# Chart 2: Monthly sales
plt.figure(figsize=(9, 5))
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
plt.close()

# Create text report
with open("report.txt", "w", encoding="utf-8") as report:
    report.write("BUSINESS DATA ANALYSIS REPORT\n")
    report.write("=" * 45 + "\n\n")
    report.write(f"Total sales: ₹{total_sales:,.2f}\n")
    report.write(f"Total quantity sold: {total_quantity}\n")
    report.write(f"Average sale value: ₹{average_sale:,.2f}\n\n")

    report.write("PRODUCT-WISE SALES\n")
    report.write("-" * 30 + "\n")
    for product, sales in product_sales.items():
        report.write(f"{product}: ₹{sales:,.2f}\n")

    report.write("\nCATEGORY-WISE SALES\n")
    report.write("-" * 30 + "\n")
    for category, sales in category_sales.items():
        report.write(f"{category}: ₹{sales:,.2f}\n")

    report.write("\nREGION-WISE SALES\n")
    report.write("-" * 30 + "\n")
    for region, sales in region_sales.items():
        report.write(f"{region}: ₹{sales:,.2f}\n")

    report.write(f"\nBest-selling product: {best_product}\n")
    report.write(f"Best-performing region: {best_region}\n")

print("\nAnalysis completed!")
print("Created: report.txt")
print("Created: charts/sales_by_category.png")
print("Created: charts/monthly_sales.png")
