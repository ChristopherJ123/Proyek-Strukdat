from Transportation import Vehicle

class Walking(Vehicle):
    def __init__(self, speed):
        super().__init__(speed, {1, 3, 4})
        self.vehicle_type = "Walking"