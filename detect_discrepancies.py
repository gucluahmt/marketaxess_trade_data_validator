import pandas as pd
import os

def detect_field_discrepancies(legacy_df, migrated_df):
    """
    Detects field-level discrepancies for matched Trade_IDs.

    Returns:
        DataFrame with columns:
        - Trade_ID
        - Field
        - Legacy_Value
        - Migrated_Value
        - Discrepancy_Flag
    """
    # Merge on Trade_ID
    merged_df = pd.merge(legacy_df, migrated_df, on="Trade_ID", suffixes=("_legacy", "_migrated"))
    result = []

    for _, row in merged_df.iterrows():
        for field in ['Price', 'Quantity']:
            legacy_val = row[f"{field}_legacy"]
            migrated_val = row[f"{field}_migrated"]

            if legacy_val != migrated_val:
                result.append({
                    'Trade_ID': row['Trade_ID'],
                    'Field': field,
                    'Legacy_Value': legacy_val,
                    'Migrated_Value': migrated_val,
                    'Discrepancy_Flag': True
                })

    return pd.DataFrame(result)

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, "..", "data")

    legacy_df = pd.read_csv(os.path.join(data_dir, "legacy_trades.csv"))
    migrated_df = pd.read_csv(os.path.join(data_dir, "migrated_trades.csv"))

    result_df = detect_field_discrepancies(legacy_df, migrated_df)
    result_df.to_csv(os.path.join(data_dir, "field_validation.csv"), index=False)

    print("✅ Field-level discrepancy check completed. Results saved to field_validation.csv")
