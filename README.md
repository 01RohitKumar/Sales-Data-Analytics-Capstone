# Sales Data Analytics Capstone Project

## 1. Project Overview
This project analyzes retail sales data to identify business performance patterns, understand profitability, and support data-driven decision-making. It includes data inspection, cleaning, exploratory data analysis (EDA), visualizations, and an interactive Power BI dashboard.

## 2. Problem Statement
The objective is to understand sales and profit performance across regions, product categories, sub-categories, and customer segments. The analysis also investigates loss-making transactions and the relationship between discounts and profit.

## 3. Dataset Description
The project uses a Sample Superstore retail sales dataset.

The dataset contains fields such as:
- Ship Mode
- Segment
- Country, City, State, Postal Code
- Region
- Category and Sub-Category
- Sales, Quantity, Discount, Profit

The original dataset contained 9,994 rows and 13 columns. After removing 17 duplicate records, the cleaned dataset contained 9,977 rows and 13 columns. No missing values were identified in the initial inspection.

## 4. Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Power BI Desktop
- Git and GitHub
- Visual Studio Code

## 5. Data Cleaning Process
- Inspected dataset structure, data types, and summary statistics.
- Checked for missing values and duplicate records.
- Removed 17 duplicate records.
- Saved the cleaned dataset as `dataset/sales_data_cleaned.csv`.
- Retained unusual values and outliers for investigation rather than automatically deleting them.

## 6. Exploratory Data Analysis (EDA)
Key metrics from the cleaned dataset:
- **Total Sales:** $2,296,195.59
- **Total Profit:** $286,241.42
- **Total Quantity Sold:** 37,820
- **Average Discount:** 15.63%
- **Loss-Making Records:** 1,869

Detailed findings are available in `report/EDA_Findings.md`.

## 7. Visualizations
Five charts were created using Python:
1. Sales by Region
2. Profit by Category
3. Top 10 Sub-Categories by Sales
4. Discount vs. Profit
5. Correlation Heatmap

The chart images are stored in the `visualizations/` folder.

## 8. Power BI Dashboard
The interactive dashboard includes:
- KPI cards for Total Sales, Total Profit, and Total Quantity Sold.
- Sales by Region.
- Sales by Category.
- Profit by Sub-Category.
- Sales by Segment.
- Slicers for Region, Category, and Segment.

Open `powerbi/Sales_Data_Analytics_Dashboard.pbix` in Power BI Desktop to explore the dashboard.

## 9. Key Business Insights
- The West region generated the highest sales and profit.
- Technology was the highest-performing category by sales and profit.
- Furniture generated substantial sales but comparatively low profit.
- A total of 1,869 records had negative profit.
- Discount and profit showed a weak negative correlation of -0.22.

## 10. Business Recommendations
- Review Furniture pricing, costs, and discount policies.
- Investigate high-discount and negative-profit transactions.
- Learn from the West region's performance.
- Monitor sales, profit, and category performance using the Power BI dashboard.

See `report/Business_Recommendations.md` for the detailed analysis.

## 11. Project Structure

```text
Sales-Data-Analytics-Capstone/
├── dataset/
│   ├── sales_data.csv
│   └── sales_data_cleaned.csv
├── notebooks/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda_analysis.py
│   └── 04_data_visualization.py
├── visualizations/
├── powerbi/
│   └── Sales_Data_Analytics_Dashboard.pbix
├── report/
│   ├── EDA_Findings.md
│   └── Business_Recommendations.md
└── README.md
```

## 12. Conclusion
This project demonstrates a complete retail data analytics workflow, from data inspection and cleaning to exploratory analysis, visualization, and interactive dashboard development. The findings highlight opportunities to investigate profitability, review discount strategies, and improve business monitoring.

## Author
Rohit Kumar
