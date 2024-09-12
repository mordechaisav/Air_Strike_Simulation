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
        self.distance_to_israel = None
        self.weather = None
