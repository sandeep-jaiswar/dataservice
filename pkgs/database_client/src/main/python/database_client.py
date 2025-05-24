# pkgs/database_client/src/main/python/database_client.py

import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
from typing import List
import os

from pkgs.data_models.historical_price_data import HistoricalPriceData

class DatabaseClient:
    """A client for interacting with the PostgreSQL database."""

    def __init__(self, db_url: str = None):
        # Use database URL from environment variable if not provided
        self.db_url = db_url if db_url else os.getenv("DATABASE_URL")
        if not self.db_url:
            raise ValueError("Database URL not provided and DATABASE_URL environment variable not set.")
        self._conn = None

    def connect(self):
        """Establishes a database connection."""
        if self._conn is None or self._conn.closed > 0:
            print(f"Connecting to database: {self.db_url}")
            try:
                self._conn = psycopg2.connect(self.db_url)
                print("Database connection established.")
            except psycopg2.OperationalError as e:
                print(f"Error connecting to database: {e}")
                self._conn = None
                raise

    def close_connection(self):
        """Closes the database connection."""
        if self._conn is not None and self._conn.closed == 0:
            print("Closing database connection.")
            self._conn.close()
            self._conn = None
            print("Database connection closed.")

    def save_historical_price_data(
        self, data: List[HistoricalPriceData]
    ) -> int:
        """Saves a list of HistoricalPriceData objects to the database.

        Returns the number of rows inserted.
        """
        if not data:
            print("No data to save.")
            return 0

        if self._conn is None or self._conn.closed > 0:
            print("Database connection not open. Cannot save data.")
            return 0

        # SQL query for inserting data. Assumes a table named 'historical_prices' exists.
        # The table should have columns matching the HistoricalPriceData attributes.
        insert_sql = sql.SQL("""
            INSERT INTO historical_prices (company_symbol, trade_date, open_price, high_price, low_price, close_price, volume, adjusted_close_price, currency)
            VALUES %s
            ON CONFLICT (company_symbol, trade_date) DO UPDATE
            SET
                open_price = EXCLUDED.open_price,
                high_price = EXCLUDED.high_price,
                low_price = EXCLUDED.low_price,
                close_price = EXCLUDED.close_price,
                volume = EXCLUDED.volume,
                adjusted_close_price = EXCLUDED.adjusted_close_price,
                currency = EXCLUDED.currency
        """)

        # Prepare data for batch insertion
        values = [
            (d.company_symbol, d.trade_date, d.open_price, d.high_price, d.low_price, d.close_price, d.volume, d.adjusted_close_price, d.currency)
            for d in data
        ]

        try:
            with self._conn.cursor() as cursor:
                # Use execute_values for efficient batch insertion
                execute_values(cursor, insert_sql, values)
                self._conn.commit()
                print(f"Successfully saved {len(data)} historical price data records.")
                return len(data)
        except psycopg2.Error as e:
            print(f"Error saving historical price data: {e}")
            self._conn.rollback()
            raise

# Note: This client assumes a table 'historical_prices' exists.
# Database migration (using Liquibase) is needed to create this table.
