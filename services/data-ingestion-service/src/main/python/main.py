# services/data-ingestion-service/src/main/python/main.py

from nse_symbols import fetch_nse_company_list
from pkgs.data_models.company import Company # Import Company model

def main():
    print("Data Ingestion Service is running!")
    print("Fetching NSE company list...")
    companies = fetch_nse_company_list()
    print("Successfully fetched company list.")
    print("Fetched companies:")
    for company in companies:
        # Access attributes using dot notation since they are Company objects
        print(f"  Symbol: {company.symbol}, Name: {company.name}")

if __name__ == "__main__":
    main()
