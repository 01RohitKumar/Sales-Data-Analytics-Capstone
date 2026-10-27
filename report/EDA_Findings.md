# Exploratory Data Analysis (EDA) — Findings

## 1. Dataset Overview
The dataset initially contained 9,994 rows and 13 columns. During data cleaning, 17 duplicate records were removed, leaving 9,977 rows. No missing values were found.

## 2. Sales and Profit Performance
Total sales were $2,296,195.59, while total profit was $286,241.42. The business sold 37,820 units, with an average discount of 15.63%.

## 3. Regional Analysis
The West region generated the highest sales of $725,255.64 and the highest profit of $108,329.81. The South region had the lowest sales at $391,721.91.

## 4. Category Analysis
Technology generated the highest sales at $836,154.03 and the highest profit at $145,454.95. Furniture generated $741,306.31 in sales but only $18,421.81 in profit, indicating a need to investigate its profitability.

## 5. Correlation Analysis
Sales and profit had a moderate positive correlation of 0.48. Discount and profit had a weak negative correlation of -0.22. These correlations show relationships in the data but do not establish causation.

## 6. Loss-Making Transactions
A total of 1,869 records had negative profit. These transactions should be investigated to understand the potential effects of discounts, product costs, and product performance.

## 7. Outlier Analysis
The IQR method identified 1,167 sales outliers, 1,881 profit outliers, and 855 discount outliers. These records were not automatically removed because they may represent genuine business transactions.

## Conclusion
The analysis shows that the West region and Technology category are major contributors to sales and profit. Furniture profitability and loss-making transactions require further investigation. These findings can help guide business recommendations and dashboard development.