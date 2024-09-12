from packages import classes,read_from_files,math_func,data_from_api
from datetime import datetime, timedelta
import requests
import csv

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
    return [list_of_airplanes, list_of_pilots, list_of_targets]



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
                selected_forecasts =({
                    'weather': forecast['weather'][0]['main'],
                    'clouds': forecast['clouds']['all'],
                    'wind_speed': forecast['wind']['speed']
                })
            if len(selected_forecasts) == 1:
                break

        target.weather = selected_forecasts

    return targets

def create_attack(airplanes, pilots, targets):
    # find the target with the high wind speed
    max_wind_speed = max(target.weather['wind_speed'] for target in targets)

    # create list of all combinations of airplanes and pilots
    all_combinations = []

    for target in targets:
        for airplane in airplanes:
            for pilot in pilots:
                priority_score = math_func.calculate_priority_score(target.priority)
                direction_score = math_func.calculate_aircraft_score(target.distance, airplane.fuel_capacity)
                weather_score = math_func.weather_score(target.weather,max_wind_speed)
                pilot_score = math_func.calculate_skill_level_score(pilot.skill)
                final_score = (priority_score + direction_score + weather_score + pilot_score) // 4
                all_combinations.append(classes.Attack(target, airplane, pilot, final_score))
    return all_combinations

def initialize_simulation():
    data = load_data()
    data[2] = calculate_distance_to_target(data[2])
    data[2] = get_weather_of_targets(data[2])
    all_combinations = create_attack(*data)
    # print all combinations to the console
    for attack in all_combinations:
        print(
            f"Target: {attack.target_city},weather: {attack.weather}, Priority: {attack.priority}, Airplane: {attack.assigned_aircraft}, Pilot: {attack.assigned_pilot}, Final Score: {attack.score}")

    read_from_files.write_to_csv(all_combinations)


initialize_simulation()















