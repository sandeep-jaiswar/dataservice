# services/data-ingestion-service/src/main/python/main.py

from nse_symbols import fetch_nse_company_list
from historical_data_fetcher import fetch_historical_price_data, get_data_file_path # Import get_data_file_path
from pkgs.data_models.company import Company
from pkgs.data_models.historical_price_data import HistoricalPriceData
from pkgs.database_client.src.main.python.database_client import DatabaseClient # Import DatabaseClient
import os


def main():
    print("Data Ingestion Service is running!")

    # Feature 1: Fetch company list
    print("Fetching NSE company list...")
    companies = fetch_nse_company_list()
    print(f"Successfully fetched {len(companies)} company(s).")
    for company in companies:
        print(f"  Symbol: {company.symbol}, Name: {company.name}")

    print("
" + "="*20 + "
") # Separator

    # Feature 2: Fetch historical price data from sample file
    print("Fetching historical price data from sample file...")
    sample_file_relative_path = "services/data-ingestion-service/historical_data_sample.json"
    sample_file_path = get_data_file_path(sample_file_relative_path)

    if not os.path.exists(sample_file_path):
         print(f"Error: Data file not found at {sample_file_path}. Cannot fetch historical data.")
         # Exit or handle error appropriately
         return

    # For demonstration, let's fetch data for a specific company from the sample
    company_to_fetch = "RELIANCE" # Example: Fetch data for Reliance
    historical_data_list = fetch_historical_price_data(sample_file_path, company_to_fetch)

    print(f"Successfully fetched {len(historical_data_list)} historical data record(s) for {company_to_fetch}.")

    print("
" + "="*20 + "
") # Separator

    # Feature 3: Save data using the DatabaseClient
    print("Saving historical data using DatabaseClient...")

    db_client = None
    try:
        db_client = DatabaseClient() # Instantiate the client (DATABASE_URL env var needed)
        db_client.connect() # Establish connection

        if historical_data_list:
            rows_saved = db_client.save_historical_price_data(historical_data_list)
            print(f"DatabaseClient reported {rows_saved} rows saved.")
        else:
            print("No historical data to save.")

    except ValueError as e:
         print(f"Configuration error for DatabaseClient: {e}")
    except psycopg2.OperationalError as e:
         print(f"Database connection failed: {e}")
    except Exception as e:
         print(f"An unexpected error occurred during database operation: {e}")
    finally:
        if db_client:
            db_client.close_connection()

    print("
" + "="*20 + "
") # Separator

    print("Data Ingestion Service finished execution.")

if __name__ == "__main__":
    main()
