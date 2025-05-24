# services/data-ingestion-service/src/test/python/integration_test.py

import unittest
from unittest.mock import patch, MagicMock
import os

# Import components from both services/packages
from services.data_ingestion_service.src.main.python.historical_data_fetcher import fetch_historical_price_data, get_data_file_path
from pkgs.database_client.src.main.python.database_client import DatabaseClient
from pkgs.data_models.historical_price_data import HistoricalPriceData

# Define a dummy database URL for the mocked client
dummy_db_url = "postgresql://dummy:dummy@localhost:5432/dummy"

class DataIngestionDatabaseIntegrationTest(unittest.TestCase):

    @patch.dict(os.environ, {'DATABASE_URL': dummy_db_url}, clear=True)
    @patch('pkgs.database_client.src.main.python.database_client.psycopg2.connect')
    @patch('pkgs.database_client.src.main.python.database_client.execute_values')
    def test_fetch_and_save_historical_data(self, mock_execute_values, mock_connect):
        # Configure the mocked database client
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        # Get the path to the sample data file using Bazel's runfiles
        sample_file_relative_path = "services/data-ingestion-service/historical_data_sample.json"
        sample_file_path = get_data_file_path(sample_file_relative_path)

        self.assertTrue(os.path.exists(sample_file_path), f"Data file not found: {sample_file_path}")

        # 1. Fetch historical data using the ingestion logic
        company_to_fetch = "RELIANCE"
        historical_data_list = fetch_historical_price_data(sample_file_path, company_to_fetch)

        self.assertGreater(len(historical_data_list), 0, "No historical data fetched")

        # 2. Simulate saving the fetched data using the database client
        db_client = DatabaseClient()
        db_client.connect()

        rows_saved = db_client.save_historical_price_data(historical_data_list)

        # Assertions to verify the interaction
        mock_connect.assert_called_once_with(dummy_db_url)
        mock_execute_values.assert_called_once()
        # Optionally, verify the data passed to execute_values
        args, kwargs = mock_execute_values.call_args
        saved_data_values = args[1]
        self.assertEqual(len(saved_data_values), len(historical_data_list))
        # You could add more specific checks on the content of saved_data_values

        mock_conn.commit.assert_called_once()
        self.assertEqual(rows_saved, len(historical_data_list), "Incorrect number of rows reported as saved")

        # Ensure connection is closed
        db_client.close_connection()
        mock_conn.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
