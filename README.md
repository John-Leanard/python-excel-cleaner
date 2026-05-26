# python-excel-cleaner

A Python script to automate the cleaning of raw sales datasets. 

This project takes messy Excel files and standardizes them for analysis. I wrote this because manually cleaning repetitive data errors—like inconsistent date formats or dirty currency strings—is inefficient and prone to human error. 

## How it works
The script processes raw Excel data through the following steps:
1. **Clean headers:** Trims whitespace, converts to lowercase, and replaces spaces with underscores.
2. **Duplicate/Blank removal:** Drops redundant rows and entries without critical information.
3. **Data formatting:** - Converts dates to datetime objects.
   - Strips currency symbols and converts strings to numeric types.
   - Cleans text formatting (strips whitespace and standardizes casing).
4. **Validation:** Saves the final clean dataset to a new Excel file.

## Requirements
- Python 3.x
- pandas
- openpyxl

Install dependencies:
```bash
pip install -r requirements.txt
