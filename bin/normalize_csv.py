import pandas as pd
import sys
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def normalize_csv(input_filepath):
    logging.info(f"Starting normalization of {input_filepath}")
    
    # Ensure the file exists
    assert os.path.isfile(input_filepath), f"File does not exist: {input_filepath}"
    
    # Load the CSV file into a DataFrame
    data = pd.read_csv(input_filepath)

    # Check for required columns
    required_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    assert all(col in data.columns for col in required_columns), "Input CSV is missing one or more required columns."

    # Additional normalization logic could go here if needed
    # For example, converting data types, handling missing values, or specific formatting

    # Save the normalized CSV
    output_filepath = input_filepath.replace('.csv', '_norm.csv')
    data.to_csv(output_filepath, index=False)
    logging.info(f"Normalized CSV saved to: {output_filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python normalize_csv.py <path to raw gainers csv>")
        sys.exit(1)

    input_csv_path = sys.argv[1]
    normalize_csv(input_csv_path)
