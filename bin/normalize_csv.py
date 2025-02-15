import os
import sys
import logging
import pandas as pd
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def normalize_csv(input_filepath):
    """
    Normalize the CSV file to ensure it has the required headers and save a new version.
    
    Args:
    input_filepath (str): The file path to the input CSV file.

    Raises:
    AssertionError: If the file does not exist or is missing required columns.
    """
    logging.info("Starting normalization of %s", input_filepath)
    # Ensure the file exists
    assert os.path.isfile(input_filepath), f"File does not exist: {input_filepath}"
    # Load the CSV file into a DataFrame
    data = pd.read_csv(input_filepath)
    # Check for required columns
    required_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    # Checking all required columns are present in the CSV
    columns_present = all(col in data.columns for col in required_columns)
    assert columns_present, (
    "Input CSV is missing one or more required columns."
    )
    # Save the normalized CSV
    output_filepath = input_filepath.replace('.csv', '_norm.csv')
    data.to_csv(output_filepath, index=False)
    logging.info("Normalized CSV saved to: %s", output_filepath)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python normalize_csv.py <path to raw gainers csv>")
        sys.exit(1)

    input_csv_path = sys.argv[1]
    normalize_csv(input_csv_path)
