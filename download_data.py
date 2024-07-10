import requests
import os
from datetime import datetime

def download_taxi_data(start_year, end_year, data_dir):
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
    current_year = datetime.now().year
    current_month = datetime.now().month

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if year == current_year and month > current_month:
                continue  # Skip months in the future
            filename = f"yellow_tripdata_{year}-{month:02d}.parquet"
            url = f"{base_url}{filename}"
            file_path = os.path.join(data_dir, filename)
            if not os.path.exists(file_path):
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    with open(file_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"Downloaded {filename}")
                else:
                    print(f"Failed to download {filename}")
            else:
                print(f"{filename} already exists. Skipping download.")
