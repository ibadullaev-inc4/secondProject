import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = os.environ.get('WEATHER_API_KEY', '')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/<city>', methods=['GET'])
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(weather)
    else:
        return jsonify({'error': 'City not found or API error'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
