# services/data-processing-service/src/main/python/main.py

from processor import process_historical_data
# Import other modules and dependencies as needed

def main():
    print("Data Processing Service is running!")

    # In a real scenario, this service would likely receive data 
    # from a message queue or read from storage.
    # For demonstration, let's simulate receiving some data.
    from pkgs.data_models.historical_price_data import HistoricalPriceData
    from datetime import date

    # Simulate receiving data (e.g., from Data Ingestion Service or Storage Service)
    simulated_raw_data = [
        HistoricalPriceData("TEST_PROC", date(2023, 11, 1), 50.0, 52.0, 49.0, 51.0, 5000),
        HistoricalPriceData("TEST_PROC", date(2023, 11, 2), 51.0, 53.0, 50.0, 52.0, 5500),
    ]

    print("Simulating receiving raw data for processing...")
    # Process the simulated data
    processed_data = process_historical_data(simulated_raw_data)

    print("
" + "="*20 + "
") # Separator

    print("Simulating sending processed data to storage or analysis service...")
    # In a real scenario, send processed_data to the Data Storage Service or Analysis Service.
    # For now, just print the processed data.
    for record in processed_data:
        print(record)

    print("
" + "="*20 + "
") # Separator

    print("Data Processing Service finished simulation.")

if __name__ == "__main__":
    main()
