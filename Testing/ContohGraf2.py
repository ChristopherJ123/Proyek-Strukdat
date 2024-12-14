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

pathAB = Path("Alfa Bravo", 1, True, 0.5)
pathBC = Path("Bravo Charlie", 1, True, 0.5)
pathCD = Path("Charlie Delta", 1, True, 0.0)
pathAE = Path("Alfa Echo", 1, True, 0.0)
pathEF = Path("Echo Foxtrot", 1, True, 0.0)
pathFG = Path("Foxtrot Golf", 1, True, 0.0)
pathGD = Path("Golf Delta", 1, True, 0.0)

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
# print(A)
# print(pathAE)
distances, predecessors = gr.shortest_times(A, Car(50, 50), Timer(hours=9, minutes=30))
print("===DISTANCES===")
for key, value in distances.items():
    print(f"{key.name}: [{value['jarak']}, {Timer(hours=value['waktu'])}]", end = " M\n" if value['jarak'] < 1000 else " KM\n")



print("===PREDECESSOR===")

for key, value in predecessors.items():
    print(f"{key.name}: {value['vertex_asal'].name if value['vertex_asal'] else None} {value['path'].road_name if value['path'] else None}")
gr.go_from_a_to_b('A', 'D', Car(50, 50), Timer(hours=9, minutes=30))