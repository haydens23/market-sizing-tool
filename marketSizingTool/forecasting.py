import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def forecast_linear(series, periods=5):
    """
    Linear extrapolation for a pandas Series.
    Returns forecasted values as a numpy array.
    """
    x = np.arange(len(series))
    y = series.values
    coef = np.polyfit(x, y, 1)
    forecast = coef[0] * (x[-1] + np.arange(1, periods + 1)) + coef[1]
    return forecast

def forecast_arima(series, periods=5):
    """
    Forecast using ARIMA. Falls back to linear if ARIMA fails.
    """
    try:
        model = ARIMA(series, order=(1, 1, 1))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=periods)
        return forecast.values
    except Exception as e:
        print(f"ARIMA failed: {e}. Using linear forecast.")
        return forecast_linear(series, periods)

if __name__ == '__main__':
    s = pd.Series([100, 110, 120, 130, 140])
    print("Linear forecast:", forecast_linear(s, 3))
    print("ARIMA forecast:", forecast_arima(s, 3))
