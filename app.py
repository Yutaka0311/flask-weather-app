from flask import Flask, render_template, request, jsonify
from config import Config
from utils.weather_api import weather_api

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    """API endpoint to fetch weather data"""
    city = request.args.get('city', '').strip()
    
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    
    weather_data = weather_api.get_weather(city)
    
    if 'error' in weather_data:
        return jsonify(weather_data), 404
    
    return jsonify(weather_data), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == "__main__":
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=5001)