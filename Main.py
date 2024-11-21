from heapq import heapify, heappop, heappush
import math
from Graph import Graph
from Vertex import Vertex


gr = Graph()

A = Vertex(0, 0, "A")
B = Vertex(3, 4, "B")
C = Vertex(5, -5, "C")
D = Vertex(5, 1, "D")
E = Vertex(12, 0, "E")
F = Vertex(8, -5, "F")
G = Vertex(9, 4, "G")
H = Vertex(8, -2, "H")

graph = {
    A : [B, C, D],
    B : [G],
    C : [F],
    D : [G, H],
    E : [],
    F : [E],
    G : [E],
    H : [C, E]
}

gr.make_graph(graph)
gr.print_graph()
distances, predecessor = gr.shortest_distances(A)
print(f"distances: {distances}")
print(f"predecessor: {predecessor}")
print("Pergi dari A ke E")
gr.go_from_a_to_b(A, E)


# format
# DijkstraAlgorithmOld
# {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf}
# {'A': 0, 'B': 4, 'C': 3, 'D': 5, 'E': 7, 'F': 8, 'G': 9, 'H': 17} {'A': None, 'B': 'A', 'C': 'A', 'D': 'A', 'E': 'B', 'F': 'E', 'G': 'C', 'H': 'F'}
# Now:
# {<Vertex.Vertex object at 0x000001C1026E2450>: 0, <Vertex.Vertex object at 0x000001C1026E2090>: 5.0, <Vertex.Vertex object at 0x000001C1026E20D0>: 7.0710678118654755, <Vertex.Vertex object at 0x000001C1042D0910>: 5.0990195135927845, <Vertex.Vertex object at 0x000001C1042D0950>: 13.81379615571165, <Vertex.Vertex object at 0x000001C1042D0B10>: 10.071067811865476, <Vertex.Vertex object at 0x000001C1042D0B50>: 10.099019513592784, <Vertex.Vertex object at 0x000001C1042D0B90>: 9.34166020071207}
# {<Vertex.Vertex object at 0x000001C1026E2450>: None, <Vertex.Vertex object at 0x000001C1026E2090>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1026E20D0>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1042D0910>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1042D0950>: <Vertex.Vertex object at 0x000001C1042D0B90>, <Vertex.Vertex object at 0x000001C1042D0B10>: <Vertex.Vertex object at 0x000001C1026E20D0>, <Vertex.Vertex object at 0x000001C1042D0B50>: <Vertex.Vertex object at 0x000001C1042D0910>, <Vertex.Vertex object at 0x000001C1042D0B90>: <Vertex.Vertex object at 0x000001C1042D0910>}
