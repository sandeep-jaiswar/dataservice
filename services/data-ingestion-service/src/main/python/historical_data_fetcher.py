# services/data-ingestion-service/src/main/python/historical_data_fetcher.py

import json
import os
from datetime import date
from typing import List

from pkgs.data_models.historical_price_data import HistoricalPriceData

# Helper to get data file path in Bazel runfiles
def get_data_file_path(relative_path):
    try:
        # Use the runfiles library for robust path resolution in Bazel
        from bazel_tools.tools.python.runfiles import runfiles
        r = runfiles.Create()
        # The path in runfiles should match the workspace path
        data_path = r.Rlocation(f"__main__/{relative_path}")
        # print(f"Resolved data path using runfiles: {data_path}") # Debugging
        return data_path
    except Exception as e:
        # Fallback for direct script execution (less reliable with Bazel run)
        print(f"Warning: Could not use runfiles library: {e}. Falling back to relative path.")
        # This fallback is primarily for local script execution outside Bazel; it's not robust.
        return relative_path

def fetch_historical_price_data(
    file_path: str,
    company_symbol: str # Added company_symbol parameter
) -> List[HistoricalPriceData]: # Added type hint for return list
    """Reads historical price data for a specific company from a JSON file."""
    print(f"Reading historical price data from: {file_path} for symbol {company_symbol}")
    data = []
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}")
        return []

    historical_data_list = []
    for item in data:
        # Filter by company_symbol
        if item.get('company_symbol') == company_symbol:
            try:
                # Basic validation and type conversion
                trade_date_str = item.get('trade_date')
                trade_date = date.fromisoformat(trade_date_str) if trade_date_str else None

                if trade_date:
                     historical_data = HistoricalPriceData(
                        company_symbol=item.get('company_symbol'),
                        trade_date=trade_date,
                        open_price=float(item.get('open_price', 0.0)),
                        high_price=float(item.get('high_price', 0.0)),
                        low_price=float(item.get('low_price', 0.0)),
                        close_price=float(item.get('close_price', 0.0)),
                        volume=int(item.get('volume', 0)),
                        adjusted_close_price=float(item.get('adjusted_close_price', 0.0)),
                        currency=item.get('currency', 'INR'),
                    )
                     historical_data_list.append(historical_data)
                else:
                     print(f"Warning: Skipping record due to invalid date: {item}")

            except (ValueError, TypeError) as e:
                print(f"Error parsing historical data record {item}: {e}")
                # Decide whether to skip or raise an error
                continue # Skip this record and continue

    print(f"Successfully read and filtered {len(historical_data_list)} historical data record(s) for {company_symbol}.")
    return historical_data_list

if __name__ == "__main__":
    # Example usage (requires the sample JSON file to be in the correct location relative to bazel-bin)
    sample_file_relative_path = "services/data-ingestion-service/historical_data_sample.json"
    sample_file_path = get_data_file_path(sample_file_relative_path)
    
    print(f"Attempting to read from: {sample_file_path}")

    if os.path.exists(sample_file_path):
        print("Fetching data for RELIANCE:")
        reliance_data = fetch_historical_price_data(sample_file_path, "RELIANCE")
        for record in reliance_data:
            print(record)

        print("
Fetching data for TCS:")
        tcs_data = fetch_historical_price_data(sample_file_path, "TCS")
        for record in tcs_data:
            print(record)
    else:
        print(f"Error: Sample data file not found at {sample_file_path}")
