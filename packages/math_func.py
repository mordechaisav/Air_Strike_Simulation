import math
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

def weather_score(weather, max_wind_speed):
    base_score = 0
    if weather["weather"] == "Clear":
        base_score = 1.0
    elif weather["weather"] == "Clouds":
        base_score = 0.7
    elif weather["weather"] == "Rain":
        base_score = 0.4
    elif weather["weather"] == "Stormy":
        base_score = 0.2
    else:
        base_score = 0
    max_clouds = 100
    cloud_score = max(0, 1 - (weather["clouds"] / max_clouds))
    wind_score = max(0, 1 - (weather["wind_speed"] / max_wind_speed))
    final_score = base_score * cloud_score * wind_score
    normalized_score = final_score * 100
    final_score = max(1, min(normalized_score, 100))
    return final_score


def calculate_aircraft_score(distance, fuel_capacity):
    if fuel_capacity - distance > 0:
        return 100
    else:
        return fuel_capacity/distance * 100



def calculate_skill_level_score(skill_level):
    max_skill_level = 10
    skill_level_score = skill_level / max_skill_level
    final_score = skill_level_score * 100

    return round(final_score)

def calculate_priority_score(priority):
    max_priority = 5
    priority_score = priority / max_priority
    final_score = priority_score * 100
    return round(final_score)