from Graph import Graph
from Path import Path
from Vertex import Vertex
from Walking import Walking
from Car import Car
from Motorcycle import Motorcycle

gr = Graph()
car = Car(50, 10)

A = Vertex(0, 0, "A")
B = Vertex(3, 4, "B")
C = Vertex(5, -5, "C")
D = Vertex(5, 1, "D")
E = Vertex(12, 0, "E")
F = Vertex(8, -5, "F")
G = Vertex(9, 4, "G")
H = Vertex(8, -2, "H")

pathAB = Path("Jl. Alfa Bravo", 1, True, 0.0)
pathAC = Path("Jl. Alfa Charlie", 1, True, 0.0)
pathAD = Path("Jl. Alfa Delta", 1, True, 0.0)

pathBG = Path("Jl. Bravo Golf", 1, True, 0.0)

pathCF = Path("Jl. Charlie Foxtrot", 1, True, 0.0)

pathDG = Path("Jl. Delta Golf", 1, True, 0.0)
pathDH = Path("Jl. Delta Hotel", 1, True, 0.0)

pathFE = Path("Jl. Foxtrot Echo", 1, True, 0.0)

pathGE = Path("Jl. Golf Echo", 1, True, 0.0)

pathHC = Path("Jl. Hotel Charlie", 1, True, 0.0)
pathHE = Path("Jl. Hotel Echo", 1, True, 0.0)


# graph = {
#     A : [B, C, D],
#     B : [G],
#     C : [F],
#     D : [G, H],
#     E : [],
#     F : [E],
#     G : [E],
#     H : [C, E]
# }

graph = {
    A : {B : pathAB, C : pathAC, D : pathAD},
    B : {G : pathBG},
    C : {F : pathCF},
    D : {G : pathDG, H : pathDH},
    E : {},
    F : {E : pathFE},
    G : {E : pathGE},
    H : {C : pathHC, E : pathHE}
}

gr.make_graph(graph)
# gr.print_graph()
distances, predecessor = gr.shortest_distances(D, car)
# print(f"distances: {distances}")
# print(f"predecessor: {predecessor}")

print("===DISTANCES===")
for key, value in distances.items():
    print(f"{key.name}: {value} KM")

print("===PREDECESSOR===")

for key, value in predecessor.items():
    print(f"{key.name}: {value[0].name if value[0] else None} {value[1].road_name if value[1] else None}")

print("Pergi dari D ke F:")
gr.go_from_a_to_b(D, F, car)


# format
# DijkstraAlgorithmOld
# {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf}
# {'A': 0, 'B': 4, 'C': 3, 'D': 5, 'E': 7, 'F': 8, 'G': 9, 'H': 17} {'A': None, 'B': 'A', 'C': 'A', 'D': 'A', 'E': 'B', 'F': 'E', 'G': 'C', 'H': 'F'}
# Now:
# {<Vertex.Vertex object at 0x000001C1026E2450>: 0, <Vertex.Vertex object at 0x000001C1026E2090>: 5.0, <Vertex.Vertex object at 0x000001C1026E20D0>: 7.0710678118654755, <Vertex.Vertex object at 0x000001C1042D0910>: 5.0990195135927845, <Vertex.Vertex object at 0x000001C1042D0950>: 13.81379615571165, <Vertex.Vertex object at 0x000001C1042D0B10>: 10.071067811865476, <Vertex.Vertex object at 0x000001C1042D0B50>: 10.099019513592784, <Vertex.Vertex object at 0x000001C1042D0B90>: 9.34166020071207}
# {<Vertex.Vertex object at 0x000001C1026E2450>: None, <Vertex.Vertex object at 0x000001C1026E2090>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1026E20D0>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1042D0910>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1042D0950>: <Vertex.Vertex object at 0x000001C1042D0B90>, <Vertex.Vertex object at 0x000001C1042D0B10>: <Vertex.Vertex object at 0x000001C1026E20D0>, <Vertex.Vertex object at 0x000001C1042D0B50>: <Vertex.Vertex object at 0x000001C1042D0910>, <Vertex.Vertex object at 0x000001C1042D0B90>: <Vertex.Vertex object at 0x000001C1042D0910>}
print()