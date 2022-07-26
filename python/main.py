from fastapi import FastAPI
from rome_weather import get_weather

app = FastAPI()


@app.get("/rome")
async def rome_weather():
    rome_lattitude, rome_longitude = '41.9028', '12.4964'
    rome_weather = await get_weather(rome_lattitude, rome_longitude)
    weather_json = rome_weather.json()
    temperature = round(weather_json['main']['temp'], 1)
    description =  weather_json['weather'][0]['description']
    return f'{temperature}°C {description}'   
  