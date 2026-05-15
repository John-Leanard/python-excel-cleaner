# =========================================================
# Professional Excel Data Cleaning Script
# Author: John Leamard M. Fajardo
# Upload this project to GitHub
# =========================================================

import pandas as pd

# -----------------------------------------
# STEP 1 — Load Excel File
# -----------------------------------------

# Replace with your Excel filename
INPUT_FILE = "messy_sales_data.xlsx"

# Output cleaned file
OUTPUT_FILE = "cleaned_sales_data.xlsx"

print("Loading Excel file...")

df = pd.read_excel(INPUT_FILE)

print("Original Shape:", df.shape)

# -----------------------------------------
# STEP 2 — Remove Completely Empty Rows
# -----------------------------------------

df = df.dropna(how="all")

# -----------------------------------------
# STEP 3 — Remove Duplicate Rows
# -----------------------------------------

before_duplicates = df.shape[0]

df = df.drop_duplicates()

after_duplicates = df.shape[0]

print(f"Removed {before_duplicates - after_duplicates} duplicate rows")

# -----------------------------------------
# STEP 4 — Clean Column Names
# -----------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Example:
# "Sales Amount" → "sales_amount"

# -----------------------------------------
# STEP 5 — Clean Text Columns
# -----------------------------------------

text_columns = ["customer_name", "region", "status"]

for col in text_columns:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

# -----------------------------------------
# STEP 6 — Fix Missing Order IDs
# -----------------------------------------

if "order_id" in df.columns:
    df["order_id"] = df["order_id"].fillna("MISSING_ID")

# -----------------------------------------
# STEP 7 — Clean Currency Values
# -----------------------------------------

if "sales_amount" in df.columns:

    df["sales_amount"] = (
        df["sales_amount"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["sales_amount"] = pd.to_numeric(
        df["sales_amount"],
        errors="coerce"
    )

# -----------------------------------------
# STEP 8 — Convert Date Columns
# -----------------------------------------

if "order_date" in df.columns:

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

# -----------------------------------------
# STEP 9 — Remove Rows With Missing Critical Data
# -----------------------------------------

critical_columns = ["customer_name", "sales_amount"]

existing_critical = [
    col for col in critical_columns
    if col in df.columns
]

df = df.dropna(subset=existing_critical)

# -----------------------------------------
# STEP 10 — Reset Index
# -----------------------------------------

df = df.reset_index(drop=True)

# -----------------------------------------
# STEP 11 — Save Cleaned Data
# -----------------------------------------

df.to_excel(OUTPUT_FILE, index=False)

# -----------------------------------------
# STEP 12 — Summary Report
# -----------------------------------------

print("\n========== CLEANING SUMMARY ==========")
print("Final Shape:", df.shape)
print("Columns:", list(df.columns))
print("Output File:", OUTPUT_FILE)
print("Data cleaning completed successfully!")
print("======================================")