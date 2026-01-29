from flask import Blueprint, jsonify, request
from services.weather_service import WeatherForecast, load_weather_data, refresh_weather_data
import os
from dotenv import load_dotenv

load_dotenv()

weather_bp = Blueprint('weather', __name__)
data = load_weather_data()

@weather_bp.route('/health', methods=['GET'])
def health_check():
    '''Health check endpoint.'''
    try:
        return jsonify({
            "status": "healthy",
            "service": "Weather API"
        })
    except Exception as e:
        return jsonify({
            'status': 'error, check api',
            'error': str(e)
        }), 500

@weather_bp.route('/weather/current', methods=['GET'])
def get_current_weather():
    '''Returns the current weather.'''
    try:
        current = data['current']

        return jsonify({
            'sucess': True,
            'data': {
                "time": current['time'],
                "temp": current['temperature_2m'],
                "wind_speed": current['wind_speed_10m'],
                "wind_direction": current['wind_direction_10m'],
                "precipitation": current['precipitation'],
            },
        })
    
    except Exception as e: 
        return jsonify({
            'success': False,
            'error' : str(e),
        }), 500
    
forecaster = WeatherForecast(data)

@weather_bp.route('/weather/daily', methods=['GET'])
def get_daily_forecast():

    try:
        days = request.args.get('days', default=1, type=int)
            
        daily_forecast = forecaster.get_daily_forecast(days=days)
        def get_day(index):
            '''helper fn: returns none if index out of bounds'''
            try:
                return daily_forecast[index]
            except IndexError:
                return None
        return jsonify({
            'success': True,
            'days': 0 if days < 1 else min(days, 3),
            'today' : get_day(0),
            'tomorrow': get_day(1),
            'day_after': get_day(2),
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@weather_bp.route('/weather/hourly', methods=['GET'])
def get_hourly_forecast():
    try:
        hourly_forecast = forecaster.get_hourly_forecast()
        return jsonify({
            'success': "True",
            "data" : hourly_forecast,
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@weather_bp.route('/weather/hourly/grouped', methods=['GET'])
def get_grouped_forecast():
    try:
        day_no = request.args.get('day_no', default=-1, type=int)
        hourly_data = forecaster.get_hourly_forecast()
        grouped_forecast = forecaster.group_forecast_by_date(hourly_data, day_no=day_no)
        return jsonify({
            'success': True,
            'data': grouped_forecast,
        })
    except Exception as e:
        return jsonify({
            'success': False,
            "error": str(e),
        }), 500


@weather_bp.route('/weather/refresh', methods=['POST'])
def refresh_weather():
    """Refresh weather data from external API"""
    try:
        # Check if request has JSON content type
        if not request.is_json:
            return jsonify({
                'success': False,
                'error': 'Content-Type must be application/json'
            }), 415  # 415 = Unsupported Media Type
        
        # Get JSON data
        data = request.get_json()  # Use get_json() instead of .json
        
        # Get lat/long from request or use default
        lat = data.get('latitude', os.getenv('LATITUDE')) if data else os.getenv('LATITUDE')
        lon = data.get('longitude', os.getenv('LONGITUDE')) if data else os.getenv('LONGITUDE')
        
        # Refresh data
        success = refresh_weather_data(latitude=lat, longitude=lon) # type: ignore
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Weather data refreshed successfully',
                'location': {'latitude': lat, 'longitude': lon}
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to refresh weather data from external API'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500