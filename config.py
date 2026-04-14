import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    FLASK_APP = 'app.py'
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('DEBUG', False)
    
    # Weather API Configuration
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    WEATHER_API_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    # Cache settings (in seconds)
    CACHE_TIMEOUT = 600  # 10 minutes
