def calculate_tam(df):
    """
    Calculates Total Addressable Market (TAM) from DataFrame.
    Example: sum of revenue for all years.
    """
    return df['Revenue'].sum()

def calculate_sam(tam, serviceable_share=0.5):
    """
    Calculates Serviceable Available Market (SAM).
    """
    return tam * serviceable_share

def calculate_som(sam, penetration_rate=0.2):
    """
    Calculates Serviceable Obtainable Market (SOM).
    """
    return sam * penetration_rate

if __name__ == '__main__':
    import pandas as pd
    df = pd.DataFrame({'Year': [2020, 2021], 'Revenue': [100, 150]})
    tam = calculate_tam(df)
    sam = calculate_sam(tam, 0.6)
    som = calculate_som(sam, 0.3)
    print(f"TAM: {tam}, SAM: {sam}, SOM: {som}")
