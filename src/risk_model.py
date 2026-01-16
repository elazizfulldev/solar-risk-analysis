import pandas as pd


def compute_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute risk score for each solar system.
    """

    # 1. QA failure flag
    df['qa_fail'] = (df['qa_status'] != 'pass').astype(int)

    # 2. Climate risk factors
    df['humidity_risk'] = (df['pvcz_humidity'] > 2).astype(int)
    df['wind_risk'] = (df['pvcz_wind'] > 2).astype(int)

    # 3. Data history risk
    df['low_history_risk'] = (df['years'] < 5).astype(int)

    # 4. Global risk score (weighted)
    df['risk_score'] = (
        df['qa_fail'] * 3 +
        df['humidity_risk'] * 1 +
        df['wind_risk'] * 1 +
        df['low_history_risk'] * 2
    )

    return df
