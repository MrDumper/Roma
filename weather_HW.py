import json, requests, pytest
from pydantic import BaseModel, field_validator
from unittest.mock import Mock, MagicMock


class Location:
    def __init__(self, longitudecls, latitudecls):
        self._longitude = longitudecls
        self._latitude = latitudecls

    def get_weather(self):
        weather_data = requests.get(
            f'https://fcc-weather-api.glitch.me/api/current?lat={self._latitude}&lon={self._longitude}')
        data = json.loads(weather_data.text)
        try:
            if weather_data.status_code != 200:
                raise Exception(f'Error request, status code : {weather_data.status_code}')
            try:
                feels_like_temp = data.get['main']['feels_like']
            except:
                feels_like_temp = 0
            dict_for_weather = {
                'temperature': {
                    'temp': data['main']['temp'],
                    'feels_like': feels_like_temp,
                    'temp_min': data['main']['temp_min'],
                    'temp_max': data['main']['temp_max']
                },
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'name': data['name']
            }
        except Exception as e:
            return None
        return WeatherPydantic(**dict_for_weather)


class TemperaturePydantic(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float

    @field_validator('temp')
    def validate_temp(cls, temp: int):
        return temp * 1.8 + 32


class WeatherPydantic(BaseModel):
    temperature: TemperaturePydantic
    pressure: float
    description: str
    name: str


# longitude = int(input('Please enter longitude: '))
# latitude = int(input('Please inter latitude: '))
loc = Location(50, 38)
weather = loc.get_weather()
print(weather)


def test_get_weather(mocker):
    mocker.patch.object(
        requests,
        'get',
        return_value=Mock(
            status_code=200,
            text=json.dumps(
                {
                    {
                        "coord": {
                            "lon": 50,
                            "lat": 28
                        }, "weather": [
                            {
                                "id": 800,
                                "main": "Clear",
                                "description": "clear sky",
                            }
                        ],
                        "base": "stations",
                        "main": {
                             "temp": 33.27,
                             "feels_like": 40.27,
                             "temp_min": 33.27,
                             "temp_max": 33.27,
                             "pressure": 1001,
                             "humidity": 72,
                             "sea_level": 1001,
                             "grnd_level": 1001
                         },
                        "visibility": 10000,
                        "wind": {
                             "speed": 3.25,
                             "deg": 258,
                             "gust": 3.6
                         },
                        "clouds": {
                             "all": 1
                         },
                        "dt": 1691623796,
                        "sys": {
                             "country": "SA",
                             "sunrise": 1691633230,
                             "sunset": 1691681029},
                        "timezone": 12600,
                        "id": 109435,
                        "name": "Jubail",
                        "cod": 200
                    }
                }
            )
        )
    )
    test_loc = Location(50, 28)
    result = test_loc.get_weather()
    expected = WeatherPydantic(
        temperature=TemperaturePydantic.model_construct(
            temp=33.27*9/5 + 32,
            feels_like=40.27,
            temp_min=33.27,
            temp_max=33.27
        ),
        pressure=1001,
        description='clear sky',
        name='Jubail',
    )
    assert result == expected