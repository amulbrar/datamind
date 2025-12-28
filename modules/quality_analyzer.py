import pandas as pd
import numpy as np

def analyze_quality(df):
    """Main function - returns quality report dict"""
    report = {}
    
    report['rows'] = len(df)
    report['columns'] = len(df.columns)
    report['missing_%'] = df.isnull().sum().sum() / (len(df) * len(df.columns)) * 100
    
    report['missing_cols'] = df.isnull().sum().to_dict()
    
    report['duplicates'] = df.duplicated().sum()
    
    report['dtypes'] = df.dtypes.value_counts().to_dict()
    
    return report

def test():
    df = pd.DataFrame({
        'name': ['A', 'B', 'C', None],
        'age': [25, None, 30, 35],
        'salary': [1000, 2000, None, 4000]
    })
    return analyze_quality(df)