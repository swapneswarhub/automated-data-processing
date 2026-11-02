
# Automated Data Processing System

A Python-based data processing project that reads structured order data, identifies data-quality issues, cleans records and generates processed output with a data-quality report.

## Project Overview

This project demonstrates basic data processing and data-quality operations using Python, Pandas and NumPy.

## Features

- Reads order data from a CSV file.
- Identifies missing values.
- Detects duplicate records.
- Performs data cleaning and processing.
- Generates a cleaned CSV output.
- Creates a data-quality report.

## Technologies Used

- Python
- Pandas
- NumPy
- CSV

## Project Structure

```text
automated-data-processing/
│
├── main.py
├── orders.csv
├── cleaned_orders.csv
├── data_quality_report.txt
└── README.md
```

## Project Results

- Input records: 10
- Duplicate records identified: 1
- Missing values identified: 2
- Records in cleaned output: 9
- Missing values remaining: 0

## How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install pandas numpy
```

3. Run the application:

```bash
python main.py
```

## Learning Outcomes

- Python-based data processing
- Working with Pandas and NumPy
- CSV file handling
- Data cleaning and validation
- Basic data-quality reporting

## Project Status

Completed: Initial data processing implementation.
