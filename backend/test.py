import requests
file_path = "weather.json"
import json

def refresh_weather_data(latitude:float, longitude:float) -> bool:
    """
    Pings Openmeteo API and stores the weather data in weather.json.

    Args:
        latitude: Location latitude
        longitude: Location longitude
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,visibility_mean&hourly=temperature_2m,uv_index&current=temperature_2m,wind_speed_10m,wind_direction_10m,precipitation&timezone=auto&forecast_days=3")

        response.raise_for_status()

        data = response.json()
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        # print('Write successful')
        return True

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch weather data: {e}")
        return False
    except IOError as e:
        print(f"Failed to write weather data: {e}")
        return False
refresh_weather_data(23.59, 58.53)

