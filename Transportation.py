class Transportation:
    def __init__(self, speed, road_compatibility, fuel_efficiency):
        self.speed = speed
        self.road_compatibility = road_compatibility
        self.fuel_efficiency= fuel_efficiency 
        self.current_location = None

    def can_traverse(self, road_type):
        return road_type in self.road_compatibility
    
    