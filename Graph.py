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
                if end not in self.graph[start]:
                    self.graph[start][end] = graph[start][end]
                self.graph[start][end].set_distance(math.sqrt(pow(abs(start.x - end.x), 2) + pow(abs(start.y - end.y), 2)))


    def add_edge(self, vertex1, vertex2, edge):
        if vertex1 not in self.graph:
            self.graph[vertex1] = {}
        self.graph[vertex1][vertex2] =  edge
        self.graph[vertex1][vertex2].set_distance(math.sqrt(pow(abs(vertex1.x - vertex2.x), 2) + pow(abs(vertex1.y - vertex2.y), 2)))


    def shortest_distances(self, source, vehicle):
        # Dijkstra Algorithm
        # Initialize the values of all nodes with infinity
        distances = {vertex: float("inf") for vertex in self.graph}
        distances[source] = 0  # Set the source value to 0

        # Initialize priority queue
        pq = [(0, source)]
        heapify(pq)

        # Set to hold visited nodes
        visited = set()

        while pq:
            current_distance, current_vertex = heappop(pq)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbour_vertex, neighbour_path in self.graph[current_vertex].items():
                # Calculate the distance from current_vertex to the neighbour_vertex
                tentative_distance = current_distance + neighbour_path.distance
                if tentative_distance < distances[neighbour_vertex]:
                    distances[neighbour_vertex] = tentative_distance
                    heappush(pq, (tentative_distance, neighbour_vertex))

        # Melihat Jalur awalnya
        predecessors = {vertex: [None, None] for vertex in self.graph}
        for vertex, distance in distances.items():
            for neighbour_vertex, neighbour_path in self.graph[vertex].items():
                if (distance + neighbour_path.distance == distances[neighbour_vertex]
                        and distances[neighbour_vertex] != float('inf')):
                    predecessors[neighbour_vertex] = [vertex, neighbour_path]

        return distances, predecessors

    def go_from_a_to_b(self, source, destination, vehicle):
        distances, predecessors = self.shortest_distances(source, vehicle)
        trace = []
        current_vertex = destination
        while predecessors[current_vertex][1] is not None:
            trace.append(predecessors[current_vertex][1])
            current_vertex = predecessors[current_vertex][0]
        trace.reverse()

        for i in range(len(trace)):
            print(trace[i].road_name if trace[i] else None)
        return trace

    def print_graph(self):
        for start, end in self.graph.items():
            for key, value in end.items():
                print(f"{start.name}, {key.name}, {value.distance}, {value.road_name}")
