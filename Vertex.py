class Vertex:

    def __init__(self, x, y, name):
        """
        Membuat Vertex baru
        :param x: Kordinat X
        :param y: Kordinat Y
        :param name: Nama Vertex
        """
        self.x = x
        self.y = y
        self.name = name


    #Entah kenapa codenya akan rusak kalau gak ada function ini, barangkali bisa tolong dijelasin sama christo
    def __lt__(self, other):
        if self.name < other.name:
            return True
        return False
