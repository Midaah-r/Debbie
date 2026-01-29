# Flask based API dev

Started as A simple api that adds the word "sigma" to every string it receives.

Now this is the backend server that collects all relevant lifestyle data, processes it and provides endpoints for the frontend application.

## Currently available endpoints: 
   - 'server health': '/api/health',
   - 'current_weather': '/api/weather/current',
   - 'daily_forecast': '/api/weather/daily?days=3 (default=1)',
   - 'hourly_forecast': '/api/weather/hourly',
   - 'grouped_hourly_forecast': '/api/weather/hourly',
   - 'refresh_data': '/api/weather/refresh (POST)'
