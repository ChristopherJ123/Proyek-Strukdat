from Transportation import Transportation

class Motorcycle(Transportation):
    def __init__(self, speed, fuel_efficiency):
        super().__init__(speed, {1, 3}, fuel_efficiency)
        self.vehicle_type = "Motorcycle"
        self.current_fuel = 5 #Liter
