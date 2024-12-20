from Transportation import Transportation

class Bicycle(Transportation): # Marco
    def __init__(self, speed):
       super().__init__(speed, {1, 3}, 0)
       self.vehicle_type = "Bicycle"
