import pandas as pd
import numpy as np

def clean_data(df, report):
    """Fixes issues from quality report"""
    df_clean = df.copy()
    
    # 1. Drop duplicates
    df_clean = df_clean.drop_duplicates()
    
    # 2. Fill missing values (simple strategy)
    for col in df_clean.columns:
        if df_clean[col].dtype == 'object':
            df_clean[col] = df_clean[col].fillna('Unknown')
        else:
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
    
    return df_clean

def test():
    df_dirty = pd.DataFrame({
        'name': ['A', 'B', None, 'A'],
        'age': [25, None, 30, 35]
    })
    report = {'missing_cols': {'name': 1, 'age': 1}}
    return clean_data(df_dirty, report).to_dict()
