import sys
sys.path.append('.')
import os
import pandas as pd
import pytest
from bin.normalize_csv import normalize_csv  # Corrected import

def test_file_not_exist():
    with pytest.raises(AssertionError):
        normalize_csv("non_existent_file.csv")  # Corrected function call

def test_output_file_creation(tmp_path):
    # Use tmp_path fixture to create a temporary CSV file
    test_input = tmp_path / "input.csv"
    test_input.write_text("symbol,price,price_change,price_percent_change\nAAPL,150,5,3.45%")
    
    expected_output = str(tmp_path / "input_norm.csv")
    normalize_csv(str(test_input))  # Corrected function call
    
    assert os.path.exists(expected_output), "Output file was not created"

def test_columns_in_output_file(tmp_path):
    # Create a sample input CSV file
    test_input = tmp_path / "input.csv"
    test_input.write_text("symbol,price,price_change,price_percent_change\nAAPL,150,5,3.45%")
    
    expected_output = str(tmp_path / "input_norm.csv")
    normalize_csv(str(test_input))  # Corrected function call
    
    # Read the output CSV and check for required columns
    data = pd.read_csv(expected_output)
    required_columns = {'symbol', 'price', 'price_change', 'price_percent_change'}
    assert required_columns <= set(data.columns), "One or more required columns are missing"
