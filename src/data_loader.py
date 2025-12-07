import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Load data from CSV.
    Adjust the delimiter if your file is comma (,) or pipe (|) separated.
    """
    # Assuming CSV, change sep='|' if it's a pipe delimited file
    df = pd.read_csv(filepath, low_memory=False)
    return df

def clean_data(df):
    """
    Perform basic data cleaning and feature engineering.
    """
    # 1. Handle Dates
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    
    # 2. Handle Categoricals
    # Ensure categorical columns are strings
    cat_cols = ['Province', 'Gender', 'VehicleType', 'Make', 'PostalCode']
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].astype(str)

    # 3. Numeric Conversions
    num_cols = ['TotalPremium', 'TotalClaims']
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 4. Feature Engineering: Margin and Loss Ratio
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    
    # Handle division by zero in LossRatio
    df['LossRatio'] = df['LossRatio'].replace([np.inf, -np.inf], 0).fillna(0)

    return df

if __name__ == "__main__":
    df = load_data('../data/insurance_claims.csv')
    df = clean_data(df)
    print(f"Data Loaded: {df.shape}")