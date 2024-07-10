import pandas as pd
import os

def save_metrics_to_csv(df, data_dir):
    # Total Acumulado de Viagens por Mês
    total_trips_per_month = df.groupby(df['tpep_pickup_datetime'].dt.to_period('M')).size().reset_index(name='total_trips')
    total_trips_per_month['tpep_pickup_datetime'] = total_trips_per_month['tpep_pickup_datetime'].dt.to_timestamp()
    total_trips_per_month.to_csv(os.path.join(data_dir, "total_trips_per_month.csv"), index=False)
    print(f"Total trips per month saved to {os.path.join(data_dir, 'total_trips_per_month.csv')}")

    # Distância Média de Viagem por Mês
    avg_trip_distance_per_month = df.groupby(df['tpep_pickup_datetime'].dt.to_period('M'))['trip_distance'].mean().reset_index(name='avg_trip_distance')
    avg_trip_distance_per_month['tpep_pickup_datetime'] = avg_trip_distance_per_month['tpep_pickup_datetime'].dt.to_timestamp()
    
    # Adicionando Média Móvel de 3 Meses
    avg_trip_distance_per_month['moving_avg_trip_distance'] = avg_trip_distance_per_month['avg_trip_distance'].rolling(window=3).mean()
    avg_trip_distance_per_month.to_csv(os.path.join(data_dir, "avg_trip_distance_per_month.csv"), index=False)
    print(f"Average trip distance per month saved to {os.path.join(data_dir, 'avg_trip_distance_per_month.csv')}")

    # Porcentagem da Receita Total por Mês
    df['month'] = df['tpep_pickup_datetime'].dt.to_period('M')
    df['year'] = df['tpep_pickup_datetime'].dt.year
    total_revenue_per_year = df.groupby('year')['total_amount'].sum().reset_index(name='total_revenue')
    revenue_per_month = df.groupby(['year', 'month'])['total_amount'].sum().reset_index(name='monthly_revenue')
    revenue_per_month = revenue_per_month.merge(total_revenue_per_year, on='year')
    revenue_per_month['revenue_percentage'] = (revenue_per_month['monthly_revenue'] / revenue_per_month['total_revenue']) * 100
    revenue_per_month['month'] = revenue_per_month['month'].dt.to_timestamp()
    revenue_per_month = revenue_per_month.drop(columns=['total_revenue'])
    revenue_per_month.to_csv(os.path.join(data_dir, "revenue_percentage_per_month.csv"), index=False)
    print(f"Revenue percentage per month saved to {os.path.join(data_dir, 'revenue_percentage_per_month.csv')}")
