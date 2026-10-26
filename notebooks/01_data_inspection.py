
import pandas as pd
from pathlib import Path

# Load the sales dataset
file_path = Path(__file__).resolve().parent.parent / "dataset" / "sales_data.csv"
df = pd.read_csv(file_path)

# Inspect the dataset
print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE (Rows, Columns)")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nNUMERICAL SUMMARY")
print(df.describe())
