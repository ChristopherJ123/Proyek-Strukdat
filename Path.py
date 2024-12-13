class Path:
    def __init__(self, road_name ,road_type, condition, congestion=0.0):
        """
        :param road_name: Nama dari jalan, misalnya 'Jl.Siwalankerto'.
        :param road_type: Tipe dari jalan, '1 : Jalan biasa', '2 : Jalan Tol', '3 : Jalan sempit/gang', '4 : Jalan pejalan kaki'.
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
        # Menghitung waktu final dengan mempertimbangkan kemacetan dan kondisi jalan
        final_time = (self.distance / base_speed) / (1 - self.congestion) if self.congestion <= 1 else 9999

        if not self.condition:  # kalo jalan buruk dikalikan 1.5
            final_time *= 1.5

        return final_time