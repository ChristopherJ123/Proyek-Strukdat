class Vertex:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name


    #Entah kenapa codenya akan rusak kalau gak ada function ini, barangkali bisa tolong dijelasin sama christo
    def __lt__(self, other):
        # Define a way to compare vertex instances. For example, by name.
        if self.name < other.name:
            return True
        return False