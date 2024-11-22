from Transportation import Vehicle

class Car(Vehicle):
    def __init__(self, speed, fuel_efficiency):
        super().__init__(speed, {0, 1})
        self.vehicle_type = "Car"
        self.fuel_efficiency = fuel_efficiency
        self.current_fuel = 100