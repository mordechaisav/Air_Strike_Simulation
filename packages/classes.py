class Pilot:
    def __init__(self,pilot_name, pilot_skill):
        self.name = pilot_name
        self.skill = pilot_skill


class Airplane:
    def __init__(self, plane_type, speed, fuel_capacity):
        self.type = plane_type
        self.speed = speed
        self.fuel_capacity = fuel_capacity


class Target:
    def __init__(self, city, priority):
        self.city = city
        self.priority = priority
        self.distance = None
        self.weather = None

class Attack:
    def __init__(self, target, airplane, pilot, score):
        self.target_city = target.city
        self.priority = target.priority
        self.assigned_pilot = pilot.name
        self.assigned_aircraft = airplane.type
        self.distance = target.distance
        self.weather = target.weather['weather']
        self.pilot_skill = pilot.skill
        self.aircraft_speed = airplane.speed
        self.fuel_capacity = airplane.fuel_capacity
        self.score = score
