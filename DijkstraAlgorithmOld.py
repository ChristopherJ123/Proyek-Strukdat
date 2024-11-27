# Ini cuma kita iseng coba coba doang, codenya nggak kepakai buat proyeknya

from heapq import heapify, heappop, heappush


class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


class Graph:
    def __init__(self, graph={}):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}

        distances[source] = 0  # Set the source value to 0
        print(distances)

        # Initialize priority queue
        pq = [(0, source)]
        heapify(pq)

        # Set to hold visited nodes
        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbour_node, neighbour_distance in self.graph[current_node].items():
                # Calculate the distance from current_node to the neighbour_node
                tentative_distance = current_distance + neighbour_distance
                if tentative_distance < distances[neighbour_node]:
                    distances[neighbour_node] = tentative_distance
                    heappush(pq, (tentative_distance, neighbour_node))

        # Melihat Jalur awalnya
        predecessors = {node: None for node in self.graph}
        for node, distance in distances.items():
            for neighbour_node, neighbour_distance in self.graph[node].items():
                if distance + neighbour_distance == distances[neighbour_node]:
                    predecessors[neighbour_node] = node

        return distances, predecessors


G = Graph()

# Cara 1
# G.add_edge("A", "B", 4)
# G.add_edge("A", "C", 3)
# G.add_edge("A", "D", 5)
#
# G.add_edge("B", "E", 3)
# G.add_edge("B", "F", 6)
#
# G.add_edge("C", "E", 6)
# G.add_edge("C", "F", 8)
# G.add_edge("C", "G", 6)
#
# G.add_edge("D", "F", 6)
# G.add_edge("D", "G", 8)
#
# G.add_edge("E", "F", 1)
# G.add_edge("E", "H", 11)
#
# G.add_edge("F", "H", 9)
#
# G.add_edge("G", "F", 2)
# G.add_edge("G", "H", 10)

# Cara 2

G.graph = {
        "A" : {"B": 4, "C": 3, "D": 5},
        "B" : {"E": 3, "F": 6},
        "C" : {"E": 6, "F": 8, "G": 6},
        "D" : {"F": 6, "G": 8},
        "E" : {"F": 1, "H": 11},
        "F" : {"H": 9},
        "G" : {"F": 2, "H": 10},
        "H" : {}
}
shortest_distances, shortest_paths = G.shortest_distances("D")

print(shortest_distances, shortest_paths)