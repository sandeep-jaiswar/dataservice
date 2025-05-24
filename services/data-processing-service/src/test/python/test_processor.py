# services/data-processing-service/src/test/python/test_processor.py

import unittest
from datetime import date

from services.data_processing_service.src.main.python.processor import process_historical_data
from pkgs.data_models.historical_price_data import HistoricalPriceData

class TestDataProcessor(unittest.TestCase):

    def test_process_historical_data_empty_list(self):
        processed_data = process_historical_data([])
        self.assertIsInstance(processed_data, list)
        self.assertEqual(len(processed_data), 0)

    def test_process_historical_data_passthrough(self):
        # Currently, the processor just passes data through.
        # This test verifies that behavior.
        input_data = [
            HistoricalPriceData("TEST_PROC", date(2023, 11, 1), 50.0, 52.0, 49.0, 51.0, 5000),
            HistoricalPriceData("TEST_PROC", date(2023, 11, 2), 51.0, 53.0, 50.0, 52.0, 5500),
        ]
        processed_data = process_historical_data(input_data)
        self.assertEqual(processed_data, input_data)

    # Add more tests here as you implement actual processing logic
    # For example, tests for moving average calculations, data cleaning, etc.

if __name__ == "__main__":
    unittest.main()
