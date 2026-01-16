import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare solar systems dataset.
    """

    # 1. Convert timestamps to datetime
    df['first_timestamp'] = pd.to_datetime(df['first_timestamp'], errors='coerce')
    df['last_timestamp'] = pd.to_datetime(df['last_timestamp'], errors='coerce')

    # 2. Drop completely empty columns (,,,,,)
    df = df.dropna(axis=1, how='all')

    # 3. Handle missing numeric values
    if 'tilt' in df.columns:
        df['tilt'] = df['tilt'].fillna(df['tilt'].median())

    # 4. Normalize text columns
    df['qa_status'] = df['qa_status'].str.lower().str.strip()
    df['tracking'] = df['tracking'].str.lower().str.strip()
    df['type'] = df['type'].str.lower().str.strip()

    # 5. Create data duration column (days)
    df['data_duration_days'] = (
        df['last_timestamp'] - df['first_timestamp']
    ).dt.days

    return df
