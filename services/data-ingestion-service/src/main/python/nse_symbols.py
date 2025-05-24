# services/data-ingestion-service/src/main/python/nse_symbols.py

from pkgs.data_models.company import Company

def fetch_nse_company_list():
    """Simulates fetching a list of NSE listed companies and returns Company objects."""
    # In a real application, this would call an external API or read from a data source.
    # For now, return a hardcoded list of example companies as Company objects.
    companies_data = [
        {"symbol": "RELIANCE", "name": "Reliance Industries Ltd"},
        {"symbol": "TCS", "name": "Tata Consultancy Services Ltd"},
        {"symbol": "HDFCBANK", "name": "HDFC Bank Ltd"},
        {"symbol": "INFY", "name": "Infosys Ltd"},
        {"symbol": "ICICIBANK", "name": "ICICI Bank Ltd"},
    ]
    
    companies = []
    for data in companies_data:
        companies.append(Company(symbol=data["symbol"], name=data["name"]))

    print("Simulating fetch of NSE company list and returning Company objects.")
    return companies

if __name__ == "__main__":
    # Example usage if running this script directly
    company_list = fetch_nse_company_list()
    print("Fetched companies (using Company model):")
    for company in company_list:
        print(f"  Symbol: {company.symbol}, Name: {company.name}")
