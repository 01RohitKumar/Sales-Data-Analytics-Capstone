
import pandas as pd
from pathlib import Path

# Define project paths
project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "dataset" / "sales_data.csv"
output_file = project_dir / "dataset" / "sales_data_cleaned.csv"

# Load original dataset
df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)

# Remove exact duplicate rows
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()

# Check missing values
print("\nMissing values after duplicate removal:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nDuplicate rows removed:", duplicate_count)
print("Cleaned dataset shape:", df.shape)
print("Cleaned dataset saved to:", output_file)
