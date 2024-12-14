from Car import Car
from Graph import Graph
from Path import Path
from Timer import Timer
from Vertex import Vertex

A = Vertex(0, 0, "A")
B = Vertex(2, 2, "B")
C = Vertex(5, 2, "C")
D = Vertex(7, 1, "D")
E = Vertex(1, -2, "E")
F = Vertex(4, -4, "F")
G = Vertex(7, -2, "G")

pathAB = Path("Alfa Bravo", 1, True, 0.0)
pathBC = Path("Bravo Charlie", 1, True, 0.0)
pathCD = Path("Charlie Delta", 1, True, 0.0)
pathAE = Path("Alfa Echo", 1, True, 0.0)
pathEF = Path("Echo Foxtrot", 1, True, 0.0)
pathFG = Path("Foxtrot Golf", 1, True, 0.0)
pathGD = Path("Golf Hotel", 1, True, 0.0)

contoh_graph2 = {
    A : {B : pathAB, E : pathAE},
    B : {C : pathBC},
    C : {D : pathCD},
    D : {},
    E : {F : pathEF},
    F : {G : pathFG},
    G : {D : pathGD}
}

gr = Graph()
gr.make_graph(contoh_graph2)
gr.go_from_a_to_b('A', 'D', Car(50, 50), Timer(hours=9, minutes=30))