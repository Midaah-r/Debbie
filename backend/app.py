# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from api.routes import weather_bp

def create_app():
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000"],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    app.config['JSON_SORT_KEYS'] = False
    app.config['DEBUG'] = True
    
    # Register blueprint with prefix
    app.register_blueprint(weather_bp, url_prefix='/api')
    
    # Add a root endpoint
    @app.route('/')
    def root():
        return jsonify({
            'message': 'Weather API is running!',
            'endpoints': {
                'server health': '/api/health',
                'current_weather': '/api/weather/current',
                'daily_forecast': '/api/weather/daily?days=3 (default=1)',
                'hourly_forecast': '/api/weather/hourly',
                'grouped_hourly_forecast': '/api/weather/hourly',
                'refresh_data': '/api/weather/refresh (POST)',
            },
            'documentation': 'Use /api prefix for all endpoints'
        })
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')