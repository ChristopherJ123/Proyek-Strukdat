from heapq import heapify, heappop, heappush
import math


class Graph:
    def __init__(self):
        self.graph = {}

    def make_graph(self, graph):
        for start, visit in graph.items():
            if start not in self.graph:
                self.graph[start] = {}
            for end in visit:
                self.graph[start][end] = math.sqrt(pow(abs(start.x - end.x), 2) + pow(abs(start.y - end.y), 2))


    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = {}
        self.graph[vertex1][vertex2] = math.sqrt(pow(abs(vertex1.x - vertex2.x), 2) + pow(abs(vertex1.y - vertex2.y), 2))


    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0

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

    def go_from_a_to_b(self, source, destination):
        distances, predecessors = self.shortest_distances(source)
        path = [destination]
        while predecessors[path[-1]] is not None:
            path.append(predecessors[path[-1]])
        path.reverse()

        for i in range(len(path)):
            print(path[i].name)
        return path

    def print_graph(self):
        for start, end in self.graph.items():
            for key, value in end.items():
                print(start.name, key.name, value)

