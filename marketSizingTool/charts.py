import matplotlib.pyplot as plt

def plot_market_history_and_forecast(years, historical, forecast, label='Revenue'):
    """
    Plots historical and forecasted values on a line chart.
    """
    all_years = list(years) + [years[-1] + i for i in range(1, len(forecast)+1)]
    all_values = list(historical) + list(forecast)
    plt.figure(figsize=(10, 5))
    plt.plot(years, historical, label='Historical')
    plt.plot(all_years[-len(forecast):], forecast, '--', label='Forecast')
    plt.xlabel('Year')
    plt.ylabel(label)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def save_plot(filename='output.png'):
    """
    Saves the current matplotlib figure.
    """
    plt.savefig(filename)

if __name__ == '__main__':
    years = [2020, 2021, 2022, 2023, 2024]
    historical = [100, 120, 140, 150, 160]
    forecast = [170, 180, 190]
    plot_market_history_and_forecast(years, historical, forecast)
    save_plot('test_output.png')
