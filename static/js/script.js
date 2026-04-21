document.addEventListener('DOMContentLoaded', () => {
    const weatherForm = document.getElementById('weatherForm');
    const cityInput = document.getElementById('cityInput');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorMessage = document.getElementById('errorMessage');
    const weatherResult = document.getElementById('weatherResult');
    
    weatherForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const city = cityInput.value.trim();
        
        if (!city) {
            showError('Please enter a city name');
            return;
        }
        
        await fetchWeather(city);
    });
    
    async function fetchWeather(city) {
        try {
            // Show loading state
            loadingSpinner.classList.remove('hidden');
            errorMessage.classList.add('hidden');
            weatherResult.classList.add('hidden');
            
            // Fetch weather data
            const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
            const data = await response.json();
            
            // Hide loading
            loadingSpinner.classList.add('hidden');
            
            if (!response.ok || data.error) {
                showError(data.error || 'Unable to fetch weather data');
                return;
            }
            
            displayWeather(data);
            
        } catch (error) {
            loadingSpinner.classList.add('hidden');
            showError('An error occurred. Please try again.');
            console.error('Fetch error:', error);
        }
    }
    
    function displayWeather(data) {   
        console.log("displayWeather動いた");
        console.log(data);
        console.log("local_time =", data.local_time);

        // Populate weather data
        document.getElementById('cityName').textContent = `${data.city}, ${data.country}`;

        document.getElementById('weatherDate').textContent = new Date().toLocaleDateString('en-US', {   
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'


        });
        document.getElementById("localTime").textContent = "Local time: " + data.local_time;
        
        document.getElementById('temperature').textContent = data.temperature;
        document.getElementById('weatherCondition').textContent = data.condition;
        document.getElementById('weatherDescription').textContent = data.description;
        
        document.getElementById('humidity').textContent = `${data.humidity}%`;
        document.getElementById('windSpeed').textContent = `${data.wind_speed} m/s`;
        document.getElementById('feelsLike').textContent = `${data.feels_like}°C`;
        document.getElementById('pressure').textContent = `${data.pressure} hPa`;
        document.getElementById('cloudiness').textContent = `${data.cloudiness}%`;
        
        // Set weather icon (OpenWeatherMap CDN)
        const iconUrl = `https://openweathermap.org/img/wn/${data.icon}@4x.png`;
        document.getElementById('weatherIcon').src = iconUrl;
        document.getElementById('weatherIcon').alt = data.description;
        
        // Show result
        weatherResult.classList.remove('hidden');
        cityInput.blur();
    }
    
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
    }
});
