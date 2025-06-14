import argparse
from marketSizingTool.data import load_csv, clean_data
from marketSizingTool.sizing import calculate_tam, calculate_sam, calculate_som
from marketSizingTool.forecasting import forecast_arima
from marketSizingTool.charts import plot_market_history_and_forecast

def main():
    parser = argparse.ArgumentParser(description="Market Sizing CLI Tool")
    parser.add_argument('--csv', required=True, help='Path to input CSV file')
    parser.add_argument('--serviceable_share', type=float, default=0.5, help='Serviceable share rate')
    parser.add_argument('--penetration', type=float, default=0.2, help='Penetration rate')
    parser.add_argument('--forecast', type=int, default=5, help='Forecast horizon (years)')
    args = parser.parse_args()

    df = load_csv(args.csv)
    df = clean_data(df)
    tam = calculate_tam(df)
    sam = calculate_sam(tam, args.serviceable_share)
    som = calculate_som(sam, args.penetration)
    print(f"TAM: {tam}\nSAM: {sam}\nSOM: {som}")
    forecast = forecast_arima(df['Revenue'], periods=args.forecast)
    plot_market_history_and_forecast(df['Year'], df['Revenue'], forecast)
    ('cli_forecast.png')
    print("Forecast plot saved as cli_forecast.png")

if __name__ == '__main__':
    main()
