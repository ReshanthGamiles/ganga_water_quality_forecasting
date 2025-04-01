import numpy as np
from sklearn.linear_model import LinearRegression

# Simulating historical data
HISTORICAL_DO = [6.8, 6.5, 6.3, 6.2, 6.0]  # Dissolved Oxygen levels
HISTORICAL_BOD = [5.0, 4.8, 4.5, 4.3, 4.0]  # BOD levels

def forecast_water_quality(historical_data):
    """Forecast next day's water quality parameters using linear regression."""
    forecast = {}
    for param, values in historical_data.items():
        x = np.array(range(len(values))).reshape(-1, 1)  # Time (days)
        y = np.array(values)  # Historical data (water quality)
        model = LinearRegression()
        model.fit(x, y)
        forecast_value = model.predict(np.array([[len(values)]]))  # Predict next value
        forecast[param] = forecast_value[0]
    
    return forecast

def generate_forecast():
    """Generate water quality forecast using historical data."""
    historical_data = {
        "DO": HISTORICAL_DO,
        "BOD": HISTORICAL_BOD
    }
    
    forecast = forecast_water_quality(historical_data)
    return forecast
