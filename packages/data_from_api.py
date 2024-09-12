import requests

def get_url_of_location(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=4982a2a3d948f64443610878443881fd'
    return url

def get_url_of_weather(city):
    url = fr'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=4982a2a3d948f64443610878443881fd'
    return url