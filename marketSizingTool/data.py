import pandas as pd

def load_csv(filepath):
    """
    Loads a CSV file and returns a pandas DataFrame.
    Raises ValueError if required columns are missing.
    """
    df = pd.read_csv(filepath)
    validate_data(df)
    return df

def validate_data(df):
    """
    Checks if DataFrame has the required columns.
    Raises ValueError if columns are missing.
    """
    required_cols = ['Year', 'Revenue']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    # Additional validation logic can go here

def clean_data(df):
    """
    Fills missing values and sorts DataFrame by Year.
    """
    df = df.dropna(subset=['Year', 'Revenue'])
    df = df.sort_values('Year').reset_index(drop=True)
    return df

if __name__ == '__main__':
    # For quick testing
    df = load_csv('../sample_data/telecom_revenue.csv')
    print(df.head())
