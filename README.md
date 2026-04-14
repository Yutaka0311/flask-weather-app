# Flask Weather App

A simple Flask web application that allows users to search for any city and displays current weather information with visual icons.

## Features

- 🔍 **City Search**: Enter any city name to get current weather
- 🌤️ **Weather Icons**: Visual weather icons from OpenWeatherMap
- 📊 **Detailed Info**: Temperature, humidity, wind speed, pressure, cloudiness, and "feels like" temperature
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile devices
- ⚡ **Real-time Data**: Fetches live weather data from OpenWeatherMap API
- 🎨 **Beautiful UI**: Modern gradient design with smooth animations

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
- **Weather Data**: OpenWeatherMap API
- **Icons**: OpenWeatherMap Weather Icons

## Installation

### 1. Clone or Download the Project

```bash
cd flask-weather-app
```

### 2. Create a Virtual Environment

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your OpenWeatherMap API key
# WEATHER_API_KEY=your_api_key_here
```

### 5. Get an OpenWeatherMap API Key

1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your free API key from the dashboard
4. Add the API key to your `.env` file

## Running the App

```bash
python app.py
```

The app will start on `http://localhost:5000`

## Usage

1. Open your browser and go to `http://localhost:5000`
2. Enter a city name in the search box
3. Click "Search" or press Enter
4. View the current weather with the weather icon

## Project Structure

```
flask-weather-app/
├── app.py                 # Flask application
├── config.py              # Configuration
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── static/
│   ├── css/
│   │   └── style.css      # Styling
│   └── js/
│       └── script.js      # Frontend interactivity
├── templates/
│   ├── base.html          # Base template
│   └── index.html         # Main page
└── utils/
    └── weather_api.py     # Weather API wrapper
```

## API Endpoints

### GET `/`
Returns the main page

### GET `/api/weather?city=<city_name>`
Returns weather data as JSON

**Example Response:**
```json
{
  "city": "London",
  "country": "GB",
  "temperature": 15,
  "feels_like": 13,
  "humidity": 65,
  "pressure": 1013,
  "wind_speed": 12.5,
  "condition": "Cloudy",
  "description": "broken clouds",
  "icon": "04d",
  "cloudiness": 75
}
```

## Error Handling

The app gracefully handles:
- Invalid city names
- Network errors
- API timeouts
- Missing or invalid API key

## Deployment

### Heroku

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Add gunicorn to requirements.txt:
```
gunicorn==20.1.0
```

3. Deploy:
```bash
git push heroku main
```

### Other Platforms

- **AWS**: Deploy using Elastic Beanstalk
- **DigitalOcean**: Use App Platform
- **PythonAnywhere**: Easy Python hosting

## Future Enhancements

- [ ] 5-day forecast
- [ ] Search history
- [ ] Favorite cities
- [ ] Dark mode toggle
- [ ] Temperature unit conversion (°C / °F)
- [ ] Geolocation support
- [ ] Weather alerts

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue on GitHub or contact the developer.

---

**Happy weather checking!** ⛅
