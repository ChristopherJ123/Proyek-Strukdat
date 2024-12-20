from Transportation import Transportation

class Bus(Transportation):  # Marco
    def __init__(self, speed, fuel_efficiency):
        super().__init__(speed, {1, 2}, fuel_efficiency)
        self.vehicle_type = "Bus"
        self.current_fuel = 100