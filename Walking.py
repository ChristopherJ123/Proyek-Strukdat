from Transportation import Vehicle

class Walking(Vehicle):
    def __init__(self, speed):
        super().__init__(speed, {1, 2, 3})
        self.vehicle_type = "Walking"