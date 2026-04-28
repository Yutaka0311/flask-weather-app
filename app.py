from flask import Flask, render_template, request, jsonify, Response
from config import Config
from utils.weather_api import weather_api
from datetime import datetime, timezone, timedelta

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/robots.txt')
def robots_txt():
    return Response("User-agent: *\nAllow: /\n", mimetype="text/plain")

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
    
  

    offset = weather_data.get("timezone", 0)

    utc_now = datetime.now(timezone.utc)

    local_time = utc_now + timedelta(seconds=offset)

    formatted_time = local_time.strftime("%Y-%m-%d %H:%M")

    weather_data["local_time"] = formatted_time
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