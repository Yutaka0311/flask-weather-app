import requests
from config import Config

class WeatherAPI:
    """Wrapper for OpenWeatherMap API"""
    
    def __init__(self):
        self.api_key = Config.WEATHER_API_KEY
        self.base_url = Config.WEATHER_API_BASE_URL
    
    def get_weather(self, city):
        """
        Fetch weather data for a given city
        
        Args:
            city (str): City name
            
        Returns:
            dict: Weather data or None if error
        """
        if not self.api_key:
            return {'error': 'API key not configured'}
        
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Use Celsius
            }
            
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            return self._format_weather_data(data)
            
        except requests.exceptions.Timeout:
            return {'error': 'Request timeout. Please try again.'}
        except requests.exceptions.ConnectionError:
            return {'error': 'Connection error. Please check your internet.'}
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                return {'error': 'City not found. Please try another city.'}
            elif response.status_code == 401:
                return {'error': 'Invalid API key.'}
            else:
                return {'error': f'HTTP error: {response.status_code}'}
        except Exception as e:
            return {'error': f'Error: {str(e)}'}
    
    def _format_weather_data(self, data):
        """
        Format raw API response into a clean dictionary
        
        Args:
            data (dict): Raw API response
            
        Returns:
            dict: Formatted weather data
        """
        try:
            return {
                'city': data.get('name'),
                'country': data.get('sys', {}).get('country'),
                'temperature': round(data.get('main', {}).get('temp', 0)),
                'feels_like': round(data.get('main', {}).get('feels_like', 0)),
                'humidity': data.get('main', {}).get('humidity'),
                'pressure': data.get('main', {}).get('pressure'),
                'wind_speed': round(data.get('wind', {}).get('speed', 0), 1),
                'condition': data.get('weather', [{}])[0].get('main'),
                'description': data.get('weather', [{}])[0].get('description'),
                'icon': data.get('weather', [{}])[0].get('icon'),
                'cloudiness': data.get('clouds', {}).get('all')
            }
        except (KeyError, IndexError, TypeError):
            return {'error': 'Error parsing weather data'}

# Create a global instance
weather_api = WeatherAPI()
