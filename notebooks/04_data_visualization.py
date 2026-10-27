
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project paths
project_dir = Path(__file__).resolve().parent.parent
data_file = project_dir / "dataset" / "sales_data_cleaned.csv"
output_dir = project_dir / "visualizations"
output_dir.mkdir(exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(data_file)

sns.set_theme(style="whitegrid")

# Chart 1: Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales (USD)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output_dir / "01_sales_by_region.png", dpi=300)
plt.close()

# Chart 2: Profit by Category
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
category_profit.plot(kind="bar")
plt.title("Total Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Profit (USD)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(output_dir / "02_profit_by_category.png", dpi=300)
plt.close()

# Chart 3: Sales by Sub-Category (Top 10)
subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
subcategory_sales.plot(kind="barh")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sales (USD)")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig(output_dir / "03_top_subcategories_sales.png", dpi=300)
plt.close()

# Chart 4: Discount vs Profit
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.4)
plt.title("Relationship Between Discount and Profit")
plt.xlabel("Discount")
plt.ylabel("Profit (USD)")
plt.tight_layout()
plt.savefig(output_dir / "04_discount_vs_profit.png", dpi=300)
plt.close()

# Chart 5: Correlation Heatmap
numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]
correlation = df[numeric_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Key Business Metrics")
plt.tight_layout()
plt.savefig(output_dir / "05_correlation_heatmap.png", dpi=300)
plt.close()

print("All 5 charts created successfully!")
print("Saved in:", output_dir)
print("\nGenerated files:")
for file in sorted(output_dir.glob("*.png")):
    print(file.name)
