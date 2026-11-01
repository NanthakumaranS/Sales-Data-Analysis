"""
Sales Data Analysis
Run from the project root:
    python notebooks/sales_analysis.py

Outputs are saved in the reports/ folder.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "dataset" / "sales_data.csv"
REPORT_DIR = PROJECT_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

# 1. Load data
df = pd.read_csv(DATA_FILE)
print("First five rows:")
print(df.head())

# 2. Clean and prepare data
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
numeric_columns = ["Quantity", "Unit_Price", "Unit_Cost"]
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.drop_duplicates()
df = df.dropna(subset=["Order_Date", "City", "Category", "Product"])
df = df[(df["Quantity"] > 0) & (df["Unit_Price"] >= 0) & (df["Unit_Cost"] >= 0)]

# 3. Create business metrics
df["Revenue"] = df["Quantity"] * df["Unit_Price"]
df["Total_Cost"] = df["Quantity"] * df["Unit_Cost"]
df["Profit"] = df["Revenue"] - df["Total_Cost"]
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

# 4. Summary KPIs
summary = pd.DataFrame({
    "Metric": ["Total Orders", "Total Units Sold", "Total Revenue", "Total Profit"],
    "Value": [df["Order_ID"].nunique(), df["Quantity"].sum(), df["Revenue"].sum(), df["Profit"].sum()]
})
summary.to_csv(REPORT_DIR / "business_summary.csv", index=False)

# 5. Analyze sales by category, city, and product
category_summary = df.groupby("Category", as_index=False)[["Quantity", "Revenue", "Profit"]].sum()
city_summary = df.groupby("City", as_index=False)[["Quantity", "Revenue", "Profit"]].sum()
product_summary = df.groupby("Product", as_index=False)[["Quantity", "Revenue", "Profit"]].sum()
monthly_summary = df.groupby("Month", as_index=False)[["Revenue", "Profit"]].sum()

category_summary.to_csv(REPORT_DIR / "sales_by_category.csv", index=False)
city_summary.to_csv(REPORT_DIR / "sales_by_city.csv", index=False)
product_summary.to_csv(REPORT_DIR / "sales_by_product.csv", index=False)
monthly_summary.to_csv(REPORT_DIR / "monthly_sales.csv", index=False)

# 6. Display key findings
print("\nBusiness summary:")
print(summary.to_string(index=False))
print("\nRevenue by category:")
print(category_summary.sort_values("Revenue", ascending=False).to_string(index=False))
print("\nRevenue by city:")
print(city_summary.sort_values("Revenue", ascending=False).to_string(index=False))

# 7. Create charts
plt.figure(figsize=(8, 5))
category_summary.sort_values("Revenue", ascending=False).plot(
    kind="bar", x="Category", y="Revenue", legend=False
)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(REPORT_DIR / "revenue_by_category.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
monthly_summary.plot(kind="line", x="Month", y="Revenue", marker="o", legend=False)
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(REPORT_DIR / "monthly_revenue.png", dpi=150)
plt.close()

print(f"\nAnalysis complete. Results saved in: {REPORT_DIR}")
