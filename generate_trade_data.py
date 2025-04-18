import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Configurable parameters
NUM_RECORDS = 100_000
MISSING_RATIO = 0.02
PRICE_VARIATION = 0.01  # 1% price difference in migrated data

# Helper to generate random dates
def generate_trade_dates(start_date, days_range, size):
    return [start_date + timedelta(days=random.randint(0, days_range)) for _ in range(size)]

# Generate base legacy dataset
def create_legacy_data():
    trade_ids = np.arange(1, NUM_RECORDS + 1)
    prices = np.round(np.random.uniform(95, 105, size=NUM_RECORDS), 2)
    quantities = np.random.randint(1, 100, size=NUM_RECORDS)
    dates = generate_trade_dates(datetime(2023, 1, 1), 90, NUM_RECORDS)

    df = pd.DataFrame({
        'Trade_ID': trade_ids,
        'Price': prices,
        'Quantity': quantities,
        'Trade_Date': dates
    })
    return df

# Create migrated data with slight variations
def create_migrated_data(legacy_df):
    df = legacy_df.copy()

    # Drop some rows to simulate missing data
    num_missing = int(len(df) * MISSING_RATIO)
    df = df.drop(df.sample(n=num_missing, random_state=42).index)

    # Modify some prices slightly
    df['Price'] = df['Price'] * (1 + np.random.uniform(-PRICE_VARIATION, PRICE_VARIATION, size=len(df)))
    df['Price'] = df['Price'].round(2)

    # Reset index
    df = df.reset_index(drop=True)
    return df

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, "..", "data")

    os.makedirs(data_dir, exist_ok=True)

    legacy_df = create_legacy_data()
    migrated_df = create_migrated_data(legacy_df)

    legacy_df.to_csv(os.path.join(data_dir, "legacy_trades.csv"), index=False)
    migrated_df.to_csv(os.path.join(data_dir, "migrated_trades.csv"), index=False)

    print("✅ Trade datasets generated successfully.")
