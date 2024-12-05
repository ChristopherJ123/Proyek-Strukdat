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
                # Ini skrg aku tambahin supaya cuma jenis kendaraan tertentu yang bisa lewat jalan tertentu
                if vehicle.can_traverse(neighbour_path.road_type):
                    tentative_distance = current_distance + neighbour_path.distance
                    if tentative_distance < distances[neighbour_vertex]:
                        distances[neighbour_vertex] = tentative_distance
                        heappush(pq, (tentative_distance, neighbour_vertex))

        # Melihat Jalur awalnya
        predecessors = {vertex: [None, None] for vertex in self.graph}
        for vertex, distance in distances.items():
            for neighbour_vertex, neighbour_path in self.graph[vertex].items():
                if (distance + neighbour_path.distance == distances[neighbour_vertex]
                        and distances[neighbour_vertex] != float('inf') and vehicle.can_traverse(neighbour_path.road_type)):
                    predecessors[neighbour_vertex] = [vertex, neighbour_path]

        return distances, predecessors

    def getNextDirection(self, startDest, middleDest, endDest):

        if (startDest.x == middleDest.x): #Jika Path Sebelumnya No Gradient (Jalan sebelumnya lurus)
            if (startDest.y > middleDest.y): #POV Top To Bottom
                if (middleDest.x > endDest.x): return "Belok Kanan Ke"
                elif (middleDest.x < endDest.x): return "Belok Kiri Ke"

            elif (startDest.y < middleDest.y): #POV Bottom To Top
                if (middleDest.x > endDest.x): return "Belok Kiri Ke"
                elif (middleDest.x < endDest.x): return "Belok Kanan Ke"

            else: return "Lurus Ke" #POV Straight

        elif (startDest.y == middleDest.y): #Jika Path Sebelumnya Zero Gradient (Jalan sebelumnya lurus)
            if (startDest.x < middleDest.x): #POV Right To Left
                if (middleDest.y > endDest.y): return "Belok Kanan Ke"
                elif (middleDest.y < endDest.y): return "Belok Kiri Ke"

            elif (startDest.x > middleDest.x): #POV Left To Right
                if (middleDest.y > endDest.y): return "Belok Kanan Ke"
                elif (middleDest.y < endDest.y): return "Belok Kiri Ke"

            else: return "Lurus Ke" #POV Straight

        else: #Jika Kedua Path Memiliki Gradien(Belok dan Belok atau bisa jadi juga Belok dan Lurus)
            gradientPrev = (middleDest.y - startDest.y) / (middleDest.x - startDest.x)

            try: #Cek jika lurusnya ke atas / bawah (No Gradient)
                gradientCurrent = (endDest.y - middleDest.y) / (endDest.x - middleDest.x)
            except:
                #Akan Turun atau Naik
                if (middleDest.y > endDest.y): return "Belok Kanan Ke"
                elif (middleDest.y < endDest.y): return "Belok Kiri Ke"
            else:
                if gradientPrev > gradientCurrent:
                    if gradientCurrent == 0 and middleDest.x > endDest.x: #Jika dari kanan(kanan turun) terus mau next jalannya lurus sebelah kiri
                        return "Belok Kiri Ke"
                    elif gradientCurrent == 0 and middleDest.x < endDest.x: #Jika dari kanan(kanan turun) terus mau next jalannya lurus sebelah kanan
                        return "Belok Kanan Ke"
                    else:return "Belok Kanan Ke" #Kanan terus kanan
                elif gradientPrev < gradientCurrent: 
                    if gradientCurrent == 0 and middleDest.x > endDest.x: #Jika dari kiri terus next(kiri naik) jalannya lurus sebelah kanan
                        return "Belok Kanan Ke"
                    elif gradientCurrent == 0 and middleDest.x < endDest.x: #Jika dari kiri terus next(kiri naik) jalannya lurus sebelah kiri
                        return "Belok Kiri Ke"
                    else:return "Belok Kiri Ke" #Kiri Kiri / Kanan Kiri
                else: return "Lurus Ke" #Lurus Lurus

    def getFirstDirection(self, startDest, endDest):
        if (startDest.x == endDest.x or startDest.y == endDest.y): return "Lurus Ke"
        elif (startDest.y > endDest.y): return "Belok Kanan Ke"
        elif (startDest.y < endDest.y): return "Belok Kiri Ke"
        

    def go_from_a_to_b(self, source, destination, vehicle):
        distances, predecessors = self.shortest_distances(source, vehicle)
        trace = []
        current_vertex = destination

        while predecessors[current_vertex][1] is not None:
            trace.append(predecessors[current_vertex])
            current_vertex = predecessors[current_vertex][0]
        
        trace.reverse()

        for i in range(len(trace)):
            if (i > 0):
                if (i+1 == len(trace)):
                    print(self.getNextDirection(trace[i - 1][0], trace[i][0], destination), end = " ")
                elif (i+1 < len(trace)): 
                    print(self.getNextDirection(trace[i - 1][0], trace[i][0], trace[i+1][0]), end = " ")

            else:
                if (i+1 == len(trace)):
                    print(self.getFirstDirection(trace[i][0], destination), end = " ")
                else:
                    print(self.getFirstDirection(trace[i][0], trace[i+1][0]), end = " ")

            # print(instruction[i] if instruction[i] else None, end = " ")
            print(trace[i][1].road_name if trace[i][1] else None)


    def print_graph(self):
        for start, end in self.graph.items():
            for key, value in end.items():
                print(f"{start.name}, {key.name}, {value.distance}, {value.road_name}")
