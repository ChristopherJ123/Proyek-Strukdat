 # Classnya udah tak buat tapi masih belum dipakai lol, bingung cara implementasiinya

class Path:
    def __init__(self, start, end, road_type, distance, condition, congestion=0.0):
        self.start = start
        self.end = end
        self.road_type = road_type
        self.distance = distance
        self.condition = condition
        self.congestion = congestion

    def travel_time(self, base_speed):

        if not self.condition:
            speed_modifier = 0.8
        else:
            speed_modifier = 1.0

        effective_speed = base_speed * speed_modifier

        effective_speed *= (1 - self.congestion)

        if effective_speed <= 0:
            raise ValueError("Effective speed too low to calculate travel time.")

        return self.distance / effective_speed