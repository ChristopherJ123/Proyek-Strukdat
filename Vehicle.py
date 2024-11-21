class Vehicle:
    def __init__(self, speed, road_compatibility):
        self.speed = speed
        self.road_compatibility = road_compatibility
        self.current_location = None

    def can_traverse(self, road_type):
        return road_type in self.road_compatibility