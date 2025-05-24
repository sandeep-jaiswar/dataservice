# services/data-ingestion-service/src/test/python/test_historical_data_fetcher.py

import unittest
import os
from datetime import date

from pkgs.data_models.historical_price_data import HistoricalPriceData
from services.data_ingestion_service.src.main.python.historical_data_fetcher import fetch_historical_price_data

# Get the path to the data file using Bazel's runfiles mechanism
# When run with `bazel test`, the file will be available relative to the test's runfiles.
# The path format is typically __main__/path/to/your/file
def get_data_file_path(relative_path):
    # This is a simplified way to get the runfiles path. A more robust way might use runfiles library.
    # For this example, we assume the test is run such that the workspace root is accessible.
    # In a real scenario, especially with more complex dependencies, use `@bazel_tools//tools/python/runfiles`
    # For now, let's construct the path assuming a standard bazel runfiles layout for simple cases.
    # The data file `historical_data_sample.json` is in `services/data-ingestion-service/`
    # and added to the `data` attribute of the test rule.
    # Inside the runfiles, it should be available at `__main__/services/data-ingestion-service/historical_data_sample.json`
    # Let's try to build the path relative to the test file's expected location in runfiles.
    # The test file is services/data-ingestion-service/src/test/python/test_historical_data_fetcher.py
    # The data file is services/data-ingestion-service/historical_data_sample.json
    # Relative path from test file to data file: ../../../historical_data_sample.json
    # However, in runfiles, the structure is flattened under __main__.
    # Let's use the absolute path from the workspace root within runfiles.

    # A more reliable way is to use the `runfiles` library provided by Bazel.
    # Since we added `@bazel_tools//tools/python/runfiles` in WORKSPACE, we can use it.
    try:
        from bazel_tools.tools.python.runfiles import runfiles
        r = runfiles.Create()
        # The path in runfiles should match the workspace path
        data_path = r.Rlocation(f"__main__/{relative_path}")
        # print(f"Resolved data path using runfiles: {data_path}") # Debugging
        return data_path
    except Exception as e:
        print(f"Warning: Could not use runfiles library: {e}. Falling back to relative path.")
        # Fallback for simpler setups or direct script execution (less reliable with Bazel)
        # Assumes the test is run from a location where the path makes sense.
        # This is fragile and should be avoided for robust Bazel tests.
        return relative_path # This will likely not work correctly with bazel test

class TestHistoricalDataFetcher(unittest.TestCase):

    def test_fetch_historical_price_data(self):
        # Path to the sample data file within the runfiles environment
        sample_file_relative_path = "services/data-ingestion-service/historical_data_sample.json"
        sample_file_path = get_data_file_path(sample_file_relative_path)

        self.assertTrue(os.path.exists(sample_file_path), f"Data file not found: {sample_file_path}")

        historical_data_list = fetch_historical_price_data(sample_file_path)

        self.assertIsInstance(historical_data_list, list)
        self.assertEqual(len(historical_data_list), 3) # Based on the sample data

        # Verify the type and basic content of the first record
        first_record = historical_data_list[0]
        self.assertIsInstance(first_record, HistoricalPriceData)
        self.assertEqual(first_record.company_symbol, "RELIANCE")
        self.assertEqual(first_record.trade_date, date(2023, 10, 26))
        self.assertEqual(first_record.open_price, 2400.0)
        self.assertEqual(first_record.volume, 1000000)

        # Verify the type and basic content of the second record
        second_record = historical_data_list[1]
        self.assertIsInstance(second_record, HistoricalPriceData)
        self.assertEqual(second_record.company_symbol, "RELIANCE")
        self.assertEqual(second_record.trade_date, date(2023, 10, 27))
        self.assertEqual(second_record.close_price, 2470.0)

        # Verify the type and basic content of the third record
        third_record = historical_data_list[2]
        self.assertIsInstance(third_record, HistoricalPriceData)
        self.assertEqual(third_record.company_symbol, "TCS")
        self.assertEqual(third_record.trade_date, date(2023, 10, 26))
        self.assertEqual(third_record.high_price, 3550.0)


if __name__ == "__main__":
    # When running directly, adjust path or ensure file is present
    # This block is mainly for direct script execution during development, not typical Bazel test runs.
    unittest.main()
