from packages import classes,read_from_files
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

def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0 # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance

def get_url_of_location(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=4982a2a3d948f64443610878443881fd'
    return url

def calculate_distance_to_target(targets):
    url_of_location_Israel = get_url_of_location('Israel')
    location_of_Israel = requests.get(url_of_location_Israel).json()[0]
    location_of_Israel= [location_of_Israel['lat'], location_of_Israel['lon']]
    for target in targets:
        url_of_location_target = get_url_of_location(target.city)
        location_of_target = requests.get(url_of_location_target).json()[0]
        location_of_target = [location_of_target['lat'], location_of_target['lon']]
        target.distance = haversine_distance(*location_of_Israel, *location_of_target)
    return location_of_Israel, targets
print(calculate_distance_to_target(load_data()[2]))







