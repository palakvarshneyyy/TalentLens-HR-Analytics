
import pandas as pd
from pathlib import Path

file_path = Path("data/raw/employee_attrition.csv")

if not file_path.exists():
    raise FileNotFoundError(f"File not found: {file_path.resolve()}")

df = pd.read_csv(file_path)

print("\n--- DATASET OVERVIEW ---")
print("Rows and columns:", df.shape)

print("\n--- FIRST FIVE RECORDS ---")
print(df.head())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- ATTRITION DISTRIBUTION ---")
print(df["Attrition"].value_counts())

print("\n--- DUPLICATE EMPLOYEE IDs ---")
print(df["EmployeeNumber"].duplicated().sum())
