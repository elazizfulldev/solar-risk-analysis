import pandas as pd


def performance_scoring(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute performance and classification metrics.
    """

    # 1. Expected production score
    df['expected_production_score'] = (
        df['dc_capacity_kW'] *
        df['pvcz_composite'] *
        df['years']
    )

    # 2. Normalize performance by capacity
    df['performance_index'] = (
        df['expected_production_score'] / df['dc_capacity_kW']
    )

    # 3. Risk classification
    def classify_risk(score):
        if score >= 5:
            return 'HIGH RISK'
        elif score >= 3:
            return 'MEDIUM RISK'
        else:
            return 'LOW RISK'

    df['risk_level'] = df['risk_score'].apply(classify_risk)

    return df
