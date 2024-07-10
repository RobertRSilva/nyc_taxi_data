from download_data import download_taxi_data
from process_data import process_data_files
from save_data import save_metrics_to_csv

import os

def main():
    start_year = 2024
    end_year = 2024
    data_dir = "./data"

    # Create data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download data
    download_taxi_data(start_year, end_year, data_dir)

    # Process data
    processed_data = process_data_files(data_dir)

    # Save metrics to CSV
    save_metrics_to_csv(processed_data, data_dir)

if __name__ == "__main__":
    main()
