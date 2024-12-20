from Transportation import Transportation

class Car(Transportation): # Marco
    def __init__(self, speed, fuel_efficiency):
        super().__init__(speed, {1, 2}, fuel_efficiency)
        self.vehicle_type = "Car"
        self.current_fuel = 40 #Liter
