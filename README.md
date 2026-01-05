# CSV Data Cleaning Tool (Python)
A practical Python tool for cleaning messy CSV files before analysis or automation.
This project demonstrates how I handle real-world data issues such as:
- duplicate records
- missing values
- inconsistent column formats
- messy text and numeric fields
The goal is to turn unreliable CSV files into clean, structured data that can be safely used for analysis, reporting, or automation workflows.
---
## What this tool does
- Removes duplicate rows
- Handles missing values (drop or fill)
- Normalizes column names
- Trims and standardizes text fields
- Prepares cleaned output CSV files
This reflects typical data-cleaning tasks I regularly solve for clients.
---
## Example use case
A client provides a CSV export from:
- CRM systems
- spreadsheets maintained by multiple people
- scraped or automatically generated data
Before any analysis or automation, the data must be cleaned.  
This tool shows a clean, repeatable approach to that process.
---
## Tech stack
- Python
- pandas
## Example usage
```python
from clean_csv import clean_csv
clean_csv(input_path="input.csv", output_path="output_clean.csv")
```
