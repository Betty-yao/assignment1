# Assignment 1: Data Cleaning Pipeline
This project is for ECON7035 Artificial Intelligence for Business, focusing on building a data cleaning pipeline for survey data.

## Project Files
- `respondent_contact.csv`: Raw survey data (contact info of respondents)
- `respondent_other.csv`: Raw survey data (other info of respondents)
- `clean.py`: Python script for data cleaning (merges data, drops missing values, filters jobs, saves cleaned data)
- `respondent_cleaned.csv`: Cleaned output data (172 rows, 7 columns)

## How to Run the Script
1. Install pandas: `pip install pandas`
2. Execute the script:  
   `python clean.py respondent_contact.csv respondent_other.csv respondent_cleaned.csv`