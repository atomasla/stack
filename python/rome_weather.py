import requests
import os

async def get_weather(lattitude, longitude):
    '''requires environment variable https://home.openweathermap.org/api_keys'''
    
    api_key = os.environ.get('WEATHER_API_KEY') 
    endpoint_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lattitude}&lon={longitude}&units=Metric&appid={api_key}'
    response = requests.get(endpoint_url)

    return response  
