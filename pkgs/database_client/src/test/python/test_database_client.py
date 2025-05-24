# pkgs/database_client/src/test/python/test_database_client.py

import unittest
from unittest.mock import patch, MagicMock
from datetime import date
import os

from pkgs.database_client.src.main.python.database_client import DatabaseClient
from pkgs.data_models.historical_price_data import HistoricalPriceData

# Define a test database URL (can be a dummy URL for mocking)
test_db_url = "postgresql://user:password@host:port/database"

class TestDatabaseClient(unittest.TestCase):

    @patch.dict(os.environ, {'DATABASE_URL': test_db_url}, clear=True)
    @patch('pkgs.database_client.src.main.python.database_client.psycopg2.connect')
    def test_connect_success(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        client = DatabaseClient()
        client.connect()

        mock_connect.assert_called_once_with(test_db_url)
        self.assertEqual(client._conn, mock_conn)
        self.assertEqual(client._conn.closed, 0) # Simulate open connection

    @patch.dict(os.environ, {}, clear=True) # Clear DATABASE_URL environment variable
    def test_init_no_db_url(self):
        with self.assertRaisesRegex(ValueError, "Database URL not provided and DATABASE_URL environment variable not set."):
            DatabaseClient()

    @patch.dict(os.environ, {'DATABASE_URL': test_db_url}, clear=True)
    @patch('pkgs.database_client.src.main.python.database_client.psycopg2.connect')
    def test_close_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        client = DatabaseClient()
        client.connect()
        client.close_connection()

        mock_conn.close.assert_called_once()
        self.assertIsNone(client._conn)

    @patch.dict(os.environ, {'DATABASE_URL': test_db_url}, clear=True)
    @patch('pkgs.database_client.src.main.python.database_client.psycopg2.connect')
    def test_save_historical_price_data_success(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        client = DatabaseClient()
        client.connect() # Ensure connection is established for saving

        historical_data_list = [
            HistoricalPriceData(
                company_symbol="TEST",
                trade_date=date(2023, 10, 26),
                open_price=100.0,
                high_price=105.0,
                low_price=98.0,
                close_price=103.0,
                volume=100000,
                adjusted_close_price=103.0,
                currency="INR",
            ),
            HistoricalPriceData(
                 company_symbol="TEST",
                 trade_date=date(2023, 10, 27),
                 open_price=104.0,
                 high_price=109.0,
                 low_price=102.0,
                 close_price=107.0,
                 volume=120000,
                 adjusted_close_price=107.0,
                 currency="INR",
            ),
        ]

        # Patch execute_values within the test method to ensure it's the one used by the client instance
        with patch('pkgs.database_client.src.main.python.database_client.execute_values') as mock_execute_values:
             rows_inserted = client.save_historical_price_data(historical_data_list)

             mock_execute_values.assert_called_once()
             # Verify the arguments passed to execute_values (basic check)
             args, kwargs = mock_execute_values.call_args
             self.assertEqual(args[1], [(d.company_symbol, d.trade_date, d.open_price, d.high_price, d.low_price, d.close_price, d.volume, d.adjusted_close_price, d.currency) for d in historical_data_list])

             mock_conn.commit.assert_called_once()
             self.assertEqual(rows_inserted, len(historical_data_list))

    @patch.dict(os.environ, {'DATABASE_URL': test_db_url}, clear=True)
    @patch('pkgs.database_client.src.main.python.database_client.psycopg2.connect')
    def test_save_historical_price_data_no_connection(self, mock_connect):
        # Do not establish a connection
        client = DatabaseClient()
        client._conn = None # Explicitly set connection to None

        historical_data_list = [
            HistoricalPriceData(
                company_symbol="TEST",
                trade_date=date(2023, 10, 26),
                open_price=100.0,
                high_price=105.0,
                low_price=98.0,
                close_price=103.0,
                volume=100000,
                adjusted_close_price=103.0,
                currency="INR",
            ),
        ]

        # Patch execute_values to ensure it's not called
        with patch('pkgs.database_client.src.main.python.database_client.execute_values') as mock_execute_values:
             rows_inserted = client.save_historical_price_data(historical_data_list)

             mock_execute_values.assert_not_called()
             self.assertEqual(rows_inserted, 0)

    @patch.dict(os.environ, {'DATABASE_URL': test_db_url}, clear=True)
    @patch('pkgs.database_client.src.main.python.database_client.psycopg2.connect')
    def test_save_historical_price_data_db_error(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        client = DatabaseClient()
        client.connect()

        historical_data_list = [
            HistoricalPriceData(
                company_symbol="TEST",
                trade_date=date(2023, 10, 26),
                open_price=100.0,
                high_price=105.0,
                low_price=98.0,
                close_price=103.0,
                volume=100000,
                adjusted_close_price=103.0,
                currency="INR",
            ),
        ]

        # Configure execute_values to raise a psycopg2 exception
        with patch('pkgs.database_client.src.main.python.database_client.execute_values') as mock_execute_values:
            mock_execute_values.side_effect = psycopg2.Error("Database error")

            with self.assertRaises(psycopg2.Error):
                 client.save_historical_price_data(historical_data_list)

            mock_conn.rollback.assert_called_once()
            mock_conn.commit.assert_not_called() # Ensure commit is not called on error


if __name__ == "__main__":
    unittest.main()
