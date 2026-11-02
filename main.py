import pandas as pd

# Read the CSV file
df = pd.read_csv("automated-data-processing/orders.csv")

# Display customer orders
print("\nCUSTOMER ORDERS DATA")
print(df)

# Count total records
print("\nTotal Records:", len(df))

# Identify missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Identify duplicate records
print("\nDUPLICATE RECORDS")
print(df.duplicated(
    subset=["Customer_Name", "Product", "Quantity", "Unit_Price", "Order_Date"]
).sum())

# Data Quality Summary
print("\n" + "=" * 40)
print("DATA QUALITY SUMMARY")
print("=" * 40)

print("Total Records:", len(df))

print("Total Missing Values:", df.isnull().sum().sum())

print("Duplicate Records:", df.duplicated(
    subset=["Customer_Name", "Product", "Quantity", "Unit_Price", "Order_Date"]
).sum())

print("=" * 40)

# Remove duplicate records
df_cleaned = df.drop_duplicates(
    subset=["Customer_Name", "Product", "Quantity", "Unit_Price", "Order_Date"]
)

print("\nDATA AFTER REMOVING DUPLICATES")
print(df_cleaned)

print("\nRecords after removing duplicates:", len(df_cleaned))

# Handle missing values

# Replace missing customer names
df_cleaned["Customer_Name"] = df_cleaned["Customer_Name"].fillna("Unknown")

# Replace missing quantities with 0
df_cleaned["Quantity"] = df_cleaned["Quantity"].fillna(0)

print("\nDATA AFTER HANDLING MISSING VALUES")
print(df_cleaned)

print("\nRemaining Missing Values:")
print(df_cleaned.isnull().sum())

# Calculate order value
df_cleaned["Order_Value"] = (
    df_cleaned["Quantity"] * df_cleaned["Unit_Price"]
)

print("\nORDER VALUE REPORT")
print(df_cleaned[["Order_ID", "Customer_Name", "Product", "Quantity", "Unit_Price", "Order_Value"]])

print("\nTotal Business Order Value:", df_cleaned["Order_Value"].sum())

#temporary check Customer
print("\nCHECK CUSTOMER NAME")
print(df_cleaned.loc[df_cleaned["Order_ID"] == 106, "Customer_Name"])

# Export cleaned data to CSV
df_cleaned.to_csv(
    "automated-data-processing/cleaned_orders.csv",
    index=False
)

print("\nCleaned data exported successfully!")
print("Output file: cleaned_orders.csv")

# Generate Data Quality Report

duplicate_count = df.duplicated(
    subset=["Customer_Name", "Product", "Quantity", "Unit_Price", "Order_Date"]
).sum()

missing_values_before = df.isnull().sum().sum()
missing_values_after = df_cleaned.isnull().sum().sum()

report = f"""
========================================
       AUTOMATED DATA QUALITY REPORT
========================================

Original Records: {len(df)}
Cleaned Records: {len(df_cleaned)}
Duplicate Records Identified: {duplicate_count}
Missing Values Identified: {missing_values_before}
Missing Values Remaining: {missing_values_after}

Total Business Order Value: Rs. {df_cleaned["Order_Value"].sum():,.2f}

========================================
"""

print(report)

# Save report to a text file
with open("automated-data-processing/data_quality_report.txt", "w") as file:
    file.write(report)

print("Data Quality Report generated successfully!")