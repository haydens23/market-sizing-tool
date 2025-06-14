import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna(subset=['Year', 'Revenue'])
    df['Year'] = df['Year'].astype(int)
    df['Revenue'] = df['Revenue'].astype(float)
    df = df.sort_values('Year')
    return df
