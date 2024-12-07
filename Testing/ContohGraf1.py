from Car import Car
from Graph import Graph
from Path import Path
from Vertex import Vertex

A = Vertex(0, 0, "A")
B = Vertex(5, 0, "B")
D = Vertex(3, 4, "D")
C = Vertex(8, 4, "C")
E = Vertex(9, 0, "E")
F = Vertex(9, -1, "F")
G = Vertex(4, -3, "G")
H = Vertex(13, -2, "H")
I = Vertex(14, -2, "I")

pathAB = Path("Alfa Bravo", 1, True, 0.0)
pathBD = Path("Bravo Delta", 1, True, 0.0)
pathBC = Path("Bravo Charlie", 1, True, 0.0)
pathBE = Path("Bravo Echo", 1, True, 0.0)
pathBF = Path("Bravo Foxtrot", 1, True, 0.0)
pathBG = Path("Bravo Golf", 1, True, 0.0)
pathFH = Path("Foxtrot Hotel", 1, True, 0.0)
pathHI = Path("Hotel Iran", 1, True, 0.0)

contoh_graph1 = {
    A : {B : pathAB},
    B : {D : pathBD, C : pathBC, E : pathBE, F : pathBF, G : pathBG},
    C : {},
    D : {},
    E : {},
    F : {H : pathFH},
    G : {},
    H : {I : pathHI},
    I : {}
}

gr = Graph()
gr.make_graph(contoh_graph1)
gr.print_graph()
gr.go_from_a_to_b(A, I, Car(50, 50))