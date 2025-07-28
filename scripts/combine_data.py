# scripts/combine_data.py
import pandas as pd
import os
import re

def clean_column_name(col_name):
    """
    Comprehensive column name cleaning:
    1. Remove parentheses and their contents
    2. Remove "Total" from the beginning
    3. Normalize line breaks and extra spaces
    4. Handle specific naming inconsistencies
    5. Normalize standalone terms to "Number of X" pattern
    
    Examples: 
    - 'Revenue (millions)' → 'Revenue'
    - 'Total Partners' → 'Number of Partners'
    - 'Net Operating\nIncome' → 'Net Operating Income'
    - 'Revenue per Lawyer (RPL)' → 'Revenue per Lawyer'
    - 'Compensation of Non-Equity Partners' → 'Compensation Non-Equity Partners'
    - 'CAP divided by number of Lawyers (VPL)' → 'Value per Lawyer'
    """
    # Convert to string and handle line breaks and extra spaces
    cleaned = str(col_name)
    
    # Replace line breaks with spaces
    cleaned = re.sub(r'\n', ' ', cleaned)
    
    # Replace multiple spaces with single space
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    # Remove parentheses and their contents
    cleaned = re.sub(r'\([^)]*\)', '', cleaned)
    
    # Remove "Total" from the beginning (handles various spacing)
    cleaned = re.sub(r'^Total\s+', '', cleaned)
    
    # Handle specific naming inconsistencies
    cleaned = cleaned.strip()
    
    # Normalize "CAP divided by number of Lawyers" to "Value per Lawyer"
    if 'CAP divided by number of Lawyers' in cleaned:
        cleaned = 'Value per Lawyer'
    
    # Normalize "Compensation of Non-Equity Partners" to standard form
    if cleaned == 'Compensation of Non-Equity Partners':
        cleaned = 'Compensation Non-Equity Partners'
    
    # Normalize standalone terms to "Number of X" pattern for consistency
    if cleaned == 'Partners':
        cleaned = 'Number of Partners'
    elif cleaned == 'Lawyers':
        cleaned = 'Number of Lawyers'
    elif cleaned == 'Offices':
        cleaned = 'Number of Offices'
    
    return cleaned.strip()

# Define the years and folder
folder = "AmLaw Yearly Data"
years = [2019, 2020, 2021, 2022, 2023, 2024]

print("🔍 Finding common columns across all files...")
print("🧹 Cleaning headers by removing parentheses...")

# First, find columns that exist in ALL files (after cleaning)
all_columns = {}
original_to_cleaned = {}  # Track mapping of original to cleaned names

for year in years:
    filepath = os.path.join(folder, f"Amlaw {year}.csv")
    df = pd.read_csv(filepath)
    
    # Clean the column names
    cleaned_columns = [clean_column_name(col) for col in df.columns]
    
    # Create mapping for this year
    year_mapping = dict(zip(df.columns, cleaned_columns))
    original_to_cleaned[year] = year_mapping
    
    # Store cleaned column names
    all_columns[year] = set(cleaned_columns)
    
    print(f"  📄 {year}: {len(df.columns)} original columns → {len(set(cleaned_columns))} unique cleaned columns")

# Find the intersection (common columns after cleaning)
common_columns = all_columns[2019]  # Start with 2019 columns
for year in years[1:]:  # Check against all other years
    common_columns = common_columns.intersection(all_columns[year])

# Convert back to list and sort for consistency
common_columns = sorted(list(common_columns))

print(f"\n✅ Found {len(common_columns)} common columns after cleaning:")
for col in common_columns:
    print(f"  - {col}")

# Now read and combine only the common columns
print(f"\n📊 Combining data with cleaned common columns...")

all_dfs = []

for year in years:
    filepath = os.path.join(folder, f"Amlaw {year}.csv")
    
    # Read the full file first
    df = pd.read_csv(filepath)
    
    # Clean column names
    df.columns = [clean_column_name(col) for col in df.columns]
    
    # Select only the common columns
    df = df[common_columns]
    
    # Add year column to track which year each row came from
    df["year"] = year
    all_dfs.append(df)
    print(f"  ✅ {year}: {len(df)} rows loaded")

# Combine all dataframes
combined_df = pd.concat(all_dfs, ignore_index=True)

# Clean up column names (lowercase, replace spaces with underscores)
combined_df.columns = combined_df.columns.str.lower().str.replace(" ", "_")

# Save the combined file
combined_df.to_csv("combined_amlaw.csv", index=False)

print(f"\n🎉 Success!")
print(f"  - Combined {len(all_dfs)} files")
print(f"  - Total rows: {len(combined_df)}")
print(f"  - Columns: {len(combined_df.columns)}")
print(f"  - Saved as: combined_amlaw.csv")

# Show a preview
print(f"\n📋 Preview of combined data:")
print(combined_df.head())