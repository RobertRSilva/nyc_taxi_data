import duckdb
import os
import pandas as pd

def process_data_files(data_dir):
    processed_data = []
    columns = [
        'VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
        'passenger_count', 'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
        'PULocationID', 'DOLocationID', 'payment_type', 'fare_amount', 'extra',
        'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
        'total_amount', 'congestion_surcharge', 'Airport_fee'
    ]

    for filename in os.listdir(data_dir):
        if filename.endswith(".parquet") and not filename.startswith("processed_data"):
            file_path = os.path.join(data_dir, filename)
            con = duckdb.connect(database=':memory:')
            
            # Inspect columns
            inspect_query = f"""
                SELECT * FROM read_parquet('{file_path}') LIMIT 1
            """
            try:
                df = con.execute(inspect_query).fetchdf()
                file_columns = list(df.columns)
                print(f"Columns in {filename}: {file_columns}")

                # Check if required columns are present
                if 'tpep_pickup_datetime' in file_columns and 'tpep_dropoff_datetime' in file_columns:
                    query = f"""
                        SELECT *
                        FROM read_parquet('{file_path}')
                        WHERE tpep_pickup_datetime IS NOT NULL
                        AND tpep_dropoff_datetime IS NOT NULL
                    """
                    result = con.execute(query).fetchall()
                    processed_data.extend(result)
                else:
                    print(f"Skipping {filename} due to missing required columns.")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    df = pd.DataFrame(processed_data, columns=columns)
    return df
