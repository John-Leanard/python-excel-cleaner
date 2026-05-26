"""
=========================================================
Professional Excel Data Cleaning Script
Author: John Leamard M. Fajardo
Description: A utility to automate cleaning messy sales datasets.
             Features: Removes duplicates/blanks, standardizes headers,
             fixes currency, parses dates, and exports cleaned data.
=========================================================
"""

import pandas as pd

# -----------------------------------------
# CONFIGURATION
# -----------------------------------------
INPUT_FILE = "messy_sales_data.xlsx"
OUTPUT_FILE = "cleaned_sales_data.xlsx"

def clean_data():
    print(f"Loading {INPUT_FILE}...")
    try:
        df = pd.read_excel(INPUT_FILE)
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found. Please ensure the file is in the directory.")
        return

    print("Original Shape:", df.shape)

    # 1. Remove Completely Empty Rows
    df = df.dropna(how="all")

    # 2. Remove Duplicate Rows
    before_duplicates = df.shape[0]
    df = df.drop_duplicates()
    print(f"Removed {before_duplicates - df.shape[0]} duplicate rows.")

    # 3. Clean Column Names (to snake_case)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # 4. Clean Text Columns
    text_columns = ["customer_name", "region", "status"]
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()

    # 5. Fix Missing Order IDs
    if "order_id" in df.columns:
        df["order_id"] = df["order_id"].fillna("MISSING_ID")

    # 6. Clean Currency Values
    if "sales_amount" in df.columns:
        df["sales_amount"] = (
            df["sales_amount"]
            .astype(str)
            .str.replace(r'[^\d.]', '', regex=True)
        )
        df["sales_amount"] = pd.to_numeric(df["sales_amount"], errors="coerce")

    # 7. Convert Date Columns
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # 8. Remove Rows With Missing Critical Data
    critical_columns = ["customer_name", "sales_amount"]
    existing_critical = [col for col in critical_columns if col in df.columns]
    df = df.dropna(subset=existing_critical)

    # 9. Final Steps
    df = df.reset_index(drop=True)
    df.to_excel(OUTPUT_FILE, index=False)

    print(f"\n========== CLEANING SUMMARY ==========")
    print(f"Final Shape: {df.shape}")
    print(f"Output File: {OUTPUT_FILE}")
    print("======================================")

if __name__ == "__main__":
    clean_data()
