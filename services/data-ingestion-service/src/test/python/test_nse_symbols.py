# services/data-ingestion-service/src/test/python/test_nse_symbols.py

import unittest
# Import the Company model for type checking
from pkgs.data_models.company import Company
from services.data_ingestion_service.src.main.python.nse_symbols import fetch_nse_company_list

class TestNseSymbols(unittest.TestCase):

    def test_fetch_nse_company_list(self):
        companies = fetch_nse_company_list()
        self.assertIsInstance(companies, list)
        self.assertGreater(len(companies), 0)
        for company in companies:
            # Assert that each item is a Company object
            self.assertIsInstance(company, Company)
            # Further checks on attributes if necessary (already done by dataclass type hints implicitly)
            self.assertIsInstance(company.symbol, str)
            self.assertIsInstance(company.name, str)
            self.assertIsNotNone(company.symbol)
            self.assertIsNotNone(company.name)

if __name__ == "__main__":
    unittest.main()
