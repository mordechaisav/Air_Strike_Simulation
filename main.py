from packages import classes,read_from_files,math_func,data_from_api
import math
import requests

airplanes_path = 'files/airplanes.json'
pilots_path = 'files/pilots.json'
targets_path = 'files/targets.json'

def load_data():
    airplanes = read_from_files.read_from_json(airplanes_path)
    list_of_airplanes = []
    for airplane in airplanes:
        airplane_obj = classes.Airplane(airplane['type'], airplane['speed'],airplane['fuel_capacity'])
        list_of_airplanes.append(airplane_obj)
    pilots = read_from_files.read_from_json(pilots_path)
    list_of_pilots = []
    for pilot in pilots:
        pilot_obj = classes.Pilot(pilot['name'], pilot['skill_level'])
        list_of_pilots.append(pilot_obj)
    targets = read_from_files.read_from_json(targets_path)
    list_of_targets = []
    for target in targets:
        target_obj = classes.Target(target['City'], target['Priority'])
        list_of_targets.append(target_obj)
    return list_of_airplanes, list_of_pilots, list_of_targets



def calculate_distance_to_target(targets):
    url_of_location_Israel = data_from_api.get_url_of_location('Israel')
    location_of_Israel = requests.get(url_of_location_Israel).json()[0]
    location_of_Israel= [location_of_Israel['lat'], location_of_Israel['lon']]
    for target in targets:
        url_of_location_target = data_from_api.get_url_of_location(target.city)
        location_of_target = requests.get(url_of_location_target).json()[0]
        location_of_target = [location_of_target['lat'], location_of_target['lon']]
        target.distance = math_func.haversine_distance(*location_of_Israel, *location_of_target)
    return targets


import requests
from datetime import datetime, timedelta

def get_weather_of_targets(targets):
    for target in targets:
        weather_url = data_from_api.get_url_of_weather(target.city)
        response = requests.get(weather_url).json()
        now = datetime.now()
        midnight = datetime(now.year, now.month, now.day) + timedelta(days=1)  # חצות הקרוב
        forecasts = response['list']
        selected_forecasts = []
        for forecast in forecasts:
            forecast_time = datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S")
            if forecast_time.hour == 0 and forecast_time >= midnight:
                selected_forecasts.append({
                    'datetime': forecast_time,
                    'weather': forecast['weather'][0]['main'],
                    'clouds': forecast['clouds']['all'],
                    'wind_speed': forecast['wind']['speed']
                })
            if len(selected_forecasts) == 3:
                break


        target.weather = selected_forecasts

    return targets

targets = load_data()[2]
targets = calculate_distance_to_target(targets)
targets = get_weather_of_targets(targets)

for forecast in targets[0].weather:
    print(f"Date: {forecast['datetime']}, Weather: {forecast['weather']}, Clouds: {forecast['clouds']}%, Wind Speed: {forecast['wind_speed']} m/s")













