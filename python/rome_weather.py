import requests
import os


def get_weather(lattitude, longitude):
    '''requires environment variable https://home.openweathermap.org/api_keys'''
    
    api_key = os.environ.get('weather_api_key') 
    endpoint_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lattitude}&lon={longitude}&units=Metric&appid={api_key}'

    response = requests.get(endpoint_url).json()
    temperature = round(response['main']['temp'], 1)
    description = response['weather'][0]['description']

    return f'{temperature}°C {description}'    


def rome_weather():

    rome_lattitude, rome_longitude = '41.9028', '12.4964'
    return get_weather(rome_lattitude, rome_longitude)
