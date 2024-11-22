from Transportation import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, speed, fuel_efficiency):
        super().__init__(speed, {1, 2})
        self.vehicle_type = "Motorcycle"
        self.fuel_efficiency = fuel_efficiency
        self.current_fuel = 100