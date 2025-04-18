import pandas as pd
import os

def compare_trade_ids(legacy_df: pd.DataFrame, migrated_df: pd.DataFrame) -> pd.DataFrame:
    """
    Compares Trade_IDs between legacy and migrated datasets.

    Returns:
        DataFrame with columns:
        - Trade_ID
        - Status: Match, Missing in Legacy, Missing in Migrated
    """
    legacy_ids = set(legacy_df['Trade_ID'])
    migrated_ids = set(migrated_df['Trade_ID'])

    all_ids = legacy_ids.union(migrated_ids)
    result = []

    for trade_id in all_ids:
        if trade_id in legacy_ids and trade_id not in migrated_ids:
            status = "Missing in Migrated"
        elif trade_id not in legacy_ids and trade_id in migrated_ids:
            status = "Missing in Legacy"
        else:
            status = "Match"
        result.append({'Trade_ID': trade_id, 'Status': status})

    return pd.DataFrame(result)

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, "..", "data")

    legacy_df = pd.read_csv(os.path.join(data_dir, "legacy_trades.csv"))
    migrated_df = pd.read_csv(os.path.join(data_dir, "migrated_trades.csv"))

    result_df = compare_trade_ids(legacy_df, migrated_df)
    result_df.to_csv(os.path.join(data_dir, "validation_result.csv"), index=False)

    print("✅ Trade ID comparison completed. Results saved to validation_result.csv")
