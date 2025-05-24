# pkgs/data_models/historical_price_data.py

from dataclasses import dataclass
from datetime import date

@dataclass
class HistoricalPriceData:
    """Represents historical price data for a company on a specific date."""
    company_symbol: str
    trade_date: date
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: int
    adjusted_close_price: float = 0.0 # Close price adjusted for splits and dividends
    currency: str = "INR" # Currency of the price data
    # Add other relevant fields as needed
