from flask import Flask, render_template, jsonify
from data_fetch import get_weather_data, get_satellite_data, get_sensor_data
from models import generate_forecast

app = Flask(__name__)

@app.route('/')
def index():
    # Get weather data (real-time)
    lat, lon = 25.1959, 80.2812  # Example coordinates for Ganga River
    weather_data = get_weather_data(lat, lon)

    # Get IoT sensor data
    sensor_data = get_sensor_data()

    # Forecast water quality
    forecast = generate_forecast()

    # Combine everything to show on the dashboard
    context = {
        "weather_data": weather_data,
        "sensor_data": sensor_data,
        "forecast": forecast
    }
    return render_template('index.html', context=context)

@app.route('/forecast')
def forecast():
    forecast = generate_forecast()
    return jsonify(forecast)

if __name__ == "__main__":
    app.run(debug=True)
