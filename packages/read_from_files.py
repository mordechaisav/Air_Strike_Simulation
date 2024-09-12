import json
import csv
def read_from_json(path):
    with open(path, 'r') as file:
        json_data = file.read()
    data = json.loads(json_data)
    return data

def write_to_csv(all_combinations):
    with open('all_combinations.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['target_city', 'priority', 'assigned_pilot', 'assigned_aircraft', 'distance', 'weather', 'pilot_skill', 'aircraft_speed', 'fuel_capacity','score'])
        for attack in all_combinations:
            writer.writerow([attack.target_city, attack.priority, attack.assigned_pilot, attack.assigned_aircraft, attack.distance, attack.weather, attack.pilot_skill, attack.aircraft_speed, attack.fuel_capacity, attack.score])