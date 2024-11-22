 # Classnya udah tak buat tapi masih belum dipakai lol, bingung cara implementasiinya

class Path:
    def __init__(self, road_name ,road_type, condition, congestion=0.0):
        """
        :param road_name: Nama dari jalan, misalnya 'Jl.Siwalankerto'.
        :param road_type: Tipe dari jalan, '1 : Jalan biasa', '2 : Jalan Tol', '3 : Jalan sempit', '4 : Jalan pejalan kaki'.
        :param condition: Kondisi dari jalan, 'True : Bagus', 'False : Buruk'.
        :param congestion: Tingkat kemacetan antara range 0.0 - 1.0. Dimana 0.0 Lancar sekali, dan 1.0 full mandek total.
        """
        self.road_name = road_name
        self.road_type = road_type
        self.condition = condition
        self.congestion = congestion

    def set_distance(self, distance):
        self.distance = distance

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