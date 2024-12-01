from heapq import heapify, heappop, heappush
import math

# sama aja cuma ganti class vehicle nya, plus hitung wktu perjalanan sm konsumsi bb
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


    def shortest_distances(self, source, Transportation):
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
                # Ini skrg aku tambahin supaya cuma jenis kendaraan tertentu yang bisa lewat jalan tertentu
                if Transportation.can_traverse(neighbour_path.road_type):
                    tentative_distance = current_distance + neighbour_path.distance
                    if tentative_distance < distances[neighbour_vertex]:
                        distances[neighbour_vertex] = tentative_distance
                        heappush(pq, (tentative_distance, neighbour_vertex))

        # Melihat Jalur awalnya
        predecessors = {vertex: [None, None] for vertex in self.graph}
        for vertex, distance in distances.items():
            for neighbour_vertex, neighbour_path in self.graph[vertex].items():
                if (distance + neighbour_path.distance == distances[neighbour_vertex]
                        and distances[neighbour_vertex] != float('inf') and Transportation.can_traverse(neighbour_path.road_type)):
                    predecessors[neighbour_vertex] = [vertex, neighbour_path]

        return distances, predecessors

    def go_from_a_to_b(self, source, destination, Transportation):
        distances, predecessors = self.shortest_distances(source, Transportation)
        trace = []
        instruction = []
        current_vertex = destination
        total_distance= 0

        while predecessors[current_vertex][1] is not None:
            trace.append(predecessors[current_vertex][1])
            total_distance += predecessors[current_vertex][1].distance

            #Kalau y nya current lebih besar dari tujuan misal A ke C(cek gambar biar paham), kiri(karena reverse)
            if (current_vertex.y > predecessors[current_vertex][0].y):
                instruction.append("Belok Kiri Ke")
            #Kalau y nya current lebih kecil dari tujuan misal C ke A(cek gambar biar paham), kanan(karena reverse)
            elif (current_vertex.y < predecessors[current_vertex][0].y):
                instruction.append("Belok Kanan Ke")
            #Kalau salah 1 sama berarti lurus aja
            elif (current_vertex.x == predecessors[current_vertex][0].x or current_vertex.y == predecessors[current_vertex][0].y):
                instruction.append("Lurus Ke")


            current_vertex = predecessors[current_vertex][0]
        trace.reverse()
        instruction.reverse()

        for i in range(len(trace)):
            print(instruction[i] if instruction[i] else None, end = " ")
            print(trace[i].road_name if trace[i] else None)
        
        # ini hehe
        if Transportation.speed <= 0: 
            print("must greater then zero!")
        else: 
            time_taken= total_distance / Transportation.speed

        fuel_consumed= total_distance * Transportation.fuel_efficiency

        print(f"\nTotal jarak: {total_distance} km")
        print(f"Estimasi waktu perjalanan: {time_taken} jam")
        print(f"Konsumsi bahan bakar: {fuel_consumed} liter")

        return trace

    def print_graph(self):
        for start, end in self.graph.items():
            for key, value in end.items():
                print(f"{start.name}, {key.name}, {value.distance}, {value.road_name}")
