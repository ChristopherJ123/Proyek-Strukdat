from Transportation import Transportation

class Walking(Transportation):
    def __init__(self, speed):
        super().__init__(speed, {1, 3, 4}, 0)
        self.vehicle_type = "Walking"
