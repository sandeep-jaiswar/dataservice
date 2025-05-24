# pkgs/data_models/src/test/python/test_models.py

import unittest
from datetime import date

from pkgs.data_models.company import Company
from pkgs.data_models.historical_price_data import HistoricalPriceData

class TestDataModels(unittest.TestCase):

    def test_company_model(self):
        company = Company(symbol="TEST", name="Test Company")
        self.assertEqual(company.symbol, "TEST")
        self.assertEqual(company.name, "Test Company")

    def test_historical_price_data_model(self):
        price_data = HistoricalPriceData(
            company_symbol="TEST",
            trade_date=date(2023, 10, 26),
            open_price=100.0,
            high_price=105.0,
            low_price=98.0,
            close_price=103.0,
            volume=100000,
        )
        self.assertEqual(price_data.company_symbol, "TEST")
        self.assertEqual(price_data.trade_date, date(2023, 10, 26))
        self.assertEqual(price_data.open_price, 100.0)
        self.assertEqual(price_data.high_price, 105.0)
        self.assertEqual(price_data.low_price, 98.0)
        self.assertEqual(price_data.close_price, 103.0)
        self.assertEqual(price_data.volume, 100000)

if __name__ == "__main__":
    unittest.main()
