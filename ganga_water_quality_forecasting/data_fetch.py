import requests
import json

API_KEY = "2565bf3633114949a4d65359253101"  # Replace with your actual API key

def get_weather_data(lat, lon):
    """Fetch weather data using an API (e.g., WeatherAPI or others)."""
    url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={lat},{lon}&days=5"
    response = requests.get(url)
    data = response.json()
    
    if "forecast" in data:
        return data["forecast"]["forecastday"]
    else:
        print("Error fetching weather data")
        return None

def get_satellite_data():
    """Placeholder for fetching satellite data. Replace with real API if available."""
    # Placeholder: Return some dummy satellite data or fetch from actual satellite APIs.
    return {"satellite_data": "dummy_data"}

def get_sensor_data():
    """Placeholder for fetching IoT sensor data."""
    # Placeholder: Replace with actual IoT sensor integration.
    return {"DO": 6.5, "BOD": 5.0, "Nitrate": 1.2}
