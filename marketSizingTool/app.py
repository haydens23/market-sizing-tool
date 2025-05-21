from flask import Flask, render_template, request
import os
from marketSizingTool.data import load_csv, clean_data
from marketSizingTool.sizing import calculate_tam, calculate_sam, calculate_som
from marketSizingTool.forecasting import forecast_arima
from marketSizingTool.charts import plot_market_history_and_forecast, save_plot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    plot_path = None
    if request.method == 'POST':
        # For now, load a sample CSV. Later, you can allow uploads!
        df = load_csv('sample_data/telecom_revenue.csv')
        df = clean_data(df)
        tam = calculate_tam(df)
        sam = calculate_sam(tam, 0.6)  # Example: 60% serviceable share
        som = calculate_som(sam, 0.3)  # Example: 30% penetration
        forecast = forecast_arima(df['Revenue'], periods=5)

        # Save plot to static/images/forecast.png
        plot_market_history_and_forecast(df['Year'], df['Revenue'], forecast)
        save_plot('static/images/forecast.png')
        plot_path = 'static/images/forecast.png'
        results = {'TAM': tam, 'SAM': sam, 'SOM': som}
    return render_template('index.html', results=results, plot_path=plot_path)

if __name__ == '__main__':
    # Run with `python -m marketSizingTool.app`
    app.run(debug=True)
