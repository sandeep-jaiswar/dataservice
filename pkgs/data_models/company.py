# pkgs/data_models/company.py

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Company:
    """Represents a company listed on the stock exchange."""
    symbol: str
    name: str
    isin: str = "" # International Securities Identification Number
    industry: str = ""
    sector: str = ""
    market_cap_inr: Optional[int] = None # Market capitalization in Indian Rupees

    # Add other relevant fields as needed
