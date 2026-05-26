# Python Excel Cleaner

A professional utility designed to automate the cleaning of messy sales datasets. This project transforms inconsistent raw data into an analysis-ready format using Python and pandas.

## Project Context & Motivation
This tool was developed to solve common data quality issues in sales reporting, such as inconsistent date formats, currency symbols in numeric fields, and duplicate records. By automating the cleaning pipeline, I reduced the time required to prepare monthly financial reports by approximately 80%.

## Key Features
* **Data Integrity:** Automatically removes duplicate records and clears empty rows.
* **Normalization:** Standardizes column names to `snake_case` to simplify database integration.
* **Data Cleansing:** Converts mixed formats into clean, machine-readable types (Dates & Currency).
* **Robustness:** Implements defensive programming techniques to handle missing values and inconsistent formatting without breaking the workflow.



## Challenges Faced
Initially, the currency column contained mixed formatting (some with symbols like '$', others without). I solved this by using Regex to strip non-numeric characters while preserving decimal points, which proved significantly more reliable than simple string replacement methods.

## Getting Started

### Prerequisites
Ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
