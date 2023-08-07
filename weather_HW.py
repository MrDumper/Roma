import json
from pydantic import BaseModel, field_validator
import requests


class Location:
    def __init__(self, longitudecls, latitudecls):
        self._longitude = longitudecls
        self._latitude = latitudecls

    def get_weather(self):
        weather_data = requests.get(f'https://fcc-weather-api.glitch.me/api/current?lat={self._latitude}&lon={self._longitude}')
        data = json.loads(weather_data.text)
        return data


class TemperaturePydantic(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float

    @field_validator('temp')
    def validate_temp(cls, temp: int):
        return temp*1.8 + 32


class WeatherPydantic(BaseModel):
    temperature: TemperaturePydantic
    pressure: float
    description: str
    name: str


longitude = int(input('Please enter longitude: '))
latitude = int(input('Please inter latitude: '))
loc = Location(longitude, latitude)
data_dict = loc.get_weather()
#print(data_dict)
keys_1 = ['weather', 'main', 'name']
keys_temperature = ['temp', 'temp_min', 'temp_max', 'feels_like']
keys_weather = ['pressure', 'description', 'name']
dict_main = {**data_dict['main']}
dict_for_temperature = {}
for key in keys_temperature:
    if key in dict_main:
        dict_for_temperature[key] = dict_main[key]
dict_for_weather = {}
for key in keys_weather:
    if key in dict_main:
        dict_for_weather[key] = dict_main[key]
    if key in data_dict:
        dict_for_weather[key] = data_dict[key]
description = data_dict.pop('weather')
desc_dict = description[0]
dict_for_weather['description'] = desc_dict['description']
temp_1 = TemperaturePydantic(**dict_for_temperature)
dict_for_weather['temperature'] = temp_1
weather = WeatherPydantic(**dict_for_weather)
print(weather)