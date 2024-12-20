class Vertex: #Christopher Joshua

    def __init__(self, x, y, name, has_lampu_lalu_lintas = False):
        """
        Membuat Vertex baru
        :param x: Kordinat X
        :param y: Kordinat Y
        :param name: Nama Vertex
        :param has_lampu_lalu_lintas: Punya lampu lalu lintas (True/False)
        """
        self.x = x
        self.y = y
        self.name = name
        self.has_lampu_lalu_lintas = has_lampu_lalu_lintas #Marco

    def __str__(self):
        return f"{{name:{self.name}, x:{self.x}, y:{self.y}}}"

    def __lt__(self, other):
        if self.name < other.name:
            return True
        return False
