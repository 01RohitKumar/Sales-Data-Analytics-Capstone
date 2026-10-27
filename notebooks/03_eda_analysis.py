
import pandas as pd
from pathlib import Path

# Project paths
project_dir = Path(__file__).resolve().parent.parent
data_file = project_dir / "dataset" / "sales_data_cleaned.csv"

# Load cleaned data
df = pd.read_csv(data_file)

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# 1. Dataset overview
print("\n1. DATASET OVERVIEW")
print("Rows and columns:", df.shape)
print("\nColumn data types:")
print(df.dtypes)

# 2. Descriptive statistics
print("\n2. DESCRIPTIVE STATISTICS")
print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())

# 3. Total business metrics
print("\n3. KEY BUSINESS METRICS")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Quantity Sold:", df["Quantity"].sum())
print("Average Discount:", round(df["Discount"].mean() * 100, 2), "%")
print("Loss-making records:", (df["Profit"] < 0).sum())

# 4. Sales and profit by region
print("\n4. REGION-WISE PERFORMANCE")
region_summary = df.groupby("Region")[["Sales", "Profit"]].sum()
print(region_summary.sort_values("Sales", ascending=False))

# 5. Category-wise performance
print("\n5. CATEGORY-WISE PERFORMANCE")
category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()
print(category_summary.sort_values("Sales", ascending=False))

# 6. Correlation analysis
print("\n6. CORRELATION MATRIX")
print(df[["Sales", "Quantity", "Discount", "Profit"]].corr().round(2))

# 7. Outlier detection using IQR
print("\n7. OUTLIER DETECTION")
for col in ["Sales", "Profit", "Discount"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = ((df[col] < lower) | (df[col] > upper)).sum()
    print(f"{col} outliers: {outliers}")

# 8. Top 5 sub-categories by sales
print("\n8. TOP 5 SUB-CATEGORIES BY SALES")
print(
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .round(2)
)

print("\nEDA completed successfully.")
