import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for web apps!
import matplotlib.pyplot as plt
import os

def plot_market_history_and_forecast(years, revenue, forecast):
    # Handle both pandas Series and numpy arrays
    if hasattr(years, 'iloc'):
        last_year = years.iloc[-1]
    else:
        last_year = years[-1]
    all_years = list(years) + [last_year + i for i in range(1, len(forecast) + 1)]
    all_revenue = list(revenue) + list(forecast)

    plt.figure(figsize=(8, 4))
    plt.plot(list(years), list(revenue), marker='o', label='Actual')
    plt.plot(all_years[-len(forecast):], forecast, marker='x', linestyle='--', label='Forecast')
    plt.xlabel('Year')
    plt.ylabel('Revenue')
    plt.title('Market Revenue History & Forecast')
    plt.legend()
    plt.tight_layout()
    img_dir = 'static/images'
    os.makedirs(img_dir, exist_ok=True)
    plt.savefig(os.path.join(img_dir, 'forecast.png'))
    plt.close()
