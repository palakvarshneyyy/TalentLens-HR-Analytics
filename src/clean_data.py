
import pandas as pd
from pathlib import Path

# Define input and output paths
input_path = Path("data/raw/employee_attrition.csv")
output_path = Path("data/processed/hr_employees_clean.csv")

# Check whether the original dataset exists
if not input_path.exists():
    raise FileNotFoundError(
        f"Dataset not found: {input_path.resolve()}"
    )

# Load the original data
df = pd.read_csv(input_path)

print("Original shape:", df.shape)

# Standardize column names for SQL and Python
df.columns = (
    df.columns
    .str.strip()
    .str.replace(r"([a-z0-9])([A-Z])", r"\1_\2", regex=True)
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

# Check for duplicate records
duplicate_rows = df.duplicated().sum()
print("Duplicate rows found:", duplicate_rows)

# Remove exact duplicate records only
df = df.drop_duplicates().copy()

# Check required columns

# Check required columns
required_columns = [
    "employee_number",
    "attrition",
    "age",
    "department",
    "job_role",
    "years_at_company",
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Required columns are missing: {missing_columns}"
    )


# Rename selected columns to readable names
df = df.rename(columns={
    "employee_number": "employee_id",
    "job_role": "job_role",
    "years_at_company": "years_at_company",
    "monthly_income": "monthly_income",
    "job_satisfaction": "job_satisfaction",
    "work_life_balance": "work_life_balance",
    "overtime": "overtime",
})


# Standardize text values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

df["attrition"] = df["attrition"].str.title()

# Validate key fields
if df["employee_id"].isna().any():
    raise ValueError("Employee IDs contain missing values.")

if df["employee_id"].duplicated().any():
    raise ValueError("Employee IDs are not unique.")

if not df["attrition"].isin(["Yes", "No"]).all():
    raise ValueError("Unexpected values in attrition column.")

# Report remaining missing values instead of silently deleting rows
missing_values = df.isnull().sum()
print("\nMissing values after cleaning:")
print(missing_values[missing_values > 0])

# Create useful analysis groups
df["age_band"] = pd.cut(
    df["age"],
    bins=[0, 24, 34, 44, 54, float("inf")],
    labels=["Under 25", "25-34", "35-44", "45-54", "55+"],
)

df["tenure_band"] = pd.cut(
    df["years_at_company"],
    bins=[-1, 1, 5, 10, float("inf")],
    labels=["0-1 years", "2-5 years", "6-10 years", "11+ years"],
)

# Create output directory if it doesn't exist
output_path.parent.mkdir(parents=True, exist_ok=True)

# Save cleaned data; preserve the raw source file
df.to_csv(output_path, index=False)

print("\nCleaned shape:", df.shape)
print("Saved cleaned data to:", output_path)
print("\nAttrition counts:")
print(df["attrition"].value_counts())
print("\nCleaning pipeline completed successfully!")
