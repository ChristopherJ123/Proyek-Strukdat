from Transportation import Transportation

class Bicycle(Transportation):
    def __init__(self, speed):
       super().__init__(speed, {1, 3})
       self.vehicle_type = "Bicycle"