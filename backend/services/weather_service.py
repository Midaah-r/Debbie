# for OpenMeteo docs: https://open-meteo.com/en/docs?latitude=23.59&longitude=58.53
import requests
import json
from collections import defaultdict


file_path = "weather.json"
# lat = "23.59"
# long = "58.53"

class WeatherForecast():
    '''Weather Forecast Class for processing data loaded (data=load_weather_data())'''
    def __init__(self, data):
        self.data: dict = data
        self.daily= data['daily']
        self.hourly= data['hourly']
        
    def get_daily_forecast(self, days: int = 3):
        """
        Get daily forecast (formatted) for specified number of days.

        Args:
            days: number of days to be forecasted (limited to 3 for now)
        Returns:
            list: list of dictionaries with {date, max temp, min temp, sunrise, sunset, visibility}
        """
        forecast = []
        for i in range(min(days, len(self.daily['time']))):
            forecast.append({
                'date': f"{self.daily['time'][i]}",
                'max_temp': f"{self.daily['temperature_2m_max'][i]} C",
                'min_temp': f"{self.daily['temperature_2m_min'][i]} C",
                'sunrise': f"{self.daily['sunrise'][i]} a.m.",
                'sunset': f"{self.daily['sunset'][i]} p.m.",
                'visibility': f"{self.daily['visibility_mean'][i]} m",
            }) 
        return forecast

    def get_hourly_forecast(self) -> list:
        """
        Get hourly forecast (formatted) for all days.

        Returns:
            list: list of dictionaries with {date, time, temp, uv_index }
        """
        hourly_forecast = []
        for i in range(len(self.hourly['time'])):
            hourly_forecast.append({
                'date': f"{self.hourly['time'][i].split('T')[0]}",
                'time': f"{self.hourly['time'][i].split('T')[1]}",
                'temp': f"{self.hourly['temperature_2m'][i]} C",
                'uv_index': f"{self.hourly['uv_index'][i]}",
            }) 
        return hourly_forecast

    def group_forecast_by_date(self, hourly_data, day_no=-1):
        """
        Groups flat hourly forecast data into a list of lists, where each sub-list contains all hourly readings for a specific date.

        Args:
            hourly_data: list of hourly data from get_hourly_forecast()
            day_no: -1 = all days, 0 = today's hourly forecast, 1 = tomorrow's, and so on
        Returns:
            list: with same dates grouped in separate arrays
        """
        try:
            grouped_map = defaultdict(list)
            
            for i in hourly_data:
                grouped_map[i['date']].append(i)
            
            forecast_grouped = list(grouped_map.values())

            if day_no == -1:
                return forecast_grouped
            else:
                return forecast_grouped[day_no]
        except IndexError as e:
            print(f"{e}, param: day_no should not exceed {len(self.daily['time'])}")

def load_weather_data() -> dict:
    """
    Load raw JSON weather data.
    """

    try:
        with open(file_path, 'r') as f:
            return(json.load(f))

    except (IOError, json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Failed to load or format weather data: {e}")
        return {"error": "Unable to load weather data"}

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
        print('Write successful')
        return True

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch weather data: {e}")
        return False
    except IOError as e:
        print(f"Failed to write weather data: {e}")
        return False
    
# # refresh_weather_data(latitude=lat, longitude=long)

# weather_data = load_weather_data()
# forecaster = WeatherForecast(weather_data)

# grouped_forecasts = forecaster.group_forecast_by_date(forecaster.get_hourly_forecast(), 0)
# # print(grouped_forecasts)
