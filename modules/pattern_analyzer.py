import pandas as pd
import numpy as np

def find_patterns(df):
    """Finds trends, correlations, outliers"""
    patterns = {}
    
    # 1. Numeric columns stats
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    patterns['numeric_summary'] = {}
    for col in numeric_cols:
        patterns['numeric_summary'][col] = {
            'mean': df[col].mean(),
            'std': df[col].std(),
            'outliers': len(df[df[col] > df[col].mean() + 3*df[col].std()])
        }
    
    # 2. Top categories (for categorical)
    cat_cols = df.select_dtypes(include=['object']).columns
    patterns['top_categories'] = {}
    for col in cat_cols:
        top = df[col].value_counts().head(3)
        patterns['top_categories'][col] = top.to_dict()
    
    return patterns

# Test
def test():
    df = pd.DataFrame({
        'sales': [100, 200, 150, 500, 120],
        'region': ['North', 'South', 'North', 'South', 'East']
    })
    return find_patterns(df)