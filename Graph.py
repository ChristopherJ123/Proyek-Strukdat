import math
from heapq import heapify, heappop, heappush

from Timer import Timer


class Graph:
    def __init__(self, scale=1.0):
        self.graph = {}
        self.scale = 1.0

    def make_graph(self, graph):
        for start, visit in graph.items():
            if start not in self.graph:
                self.graph[start] = {}
            for end in visit:
                if end not in self.graph[start]:
                    self.graph[start][end] = graph[start][end]
                self.graph[start][end].set_distance((math.sqrt(pow(abs(start.x - end.x), 2) + pow(abs(start.y - end.y), 2))) * self.scale)

        # Tambah congestion bagi edge yang menyambung ke sebuah vertex yang memiliki lampu lalu lintas dengan sekian.
        for start, visit in self.graph.items():
            for vertex_tujuan, path in visit.items():
                if vertex_tujuan.has_lampu_lalu_lintas:
                    path.congestion = min(path.congestion + (1 - path.congestion) * 0.3, 1.0)  # menambah kemacetan

    def scale_distances(self, multitude_of):
        """
        Scale the distance of each edge with the multitude of. Jangan lupa di make_graph dulu.
        :param multitude_of: multitude
        """
        self.scale *= multitude_of
        for start, visit in self.graph.items():
            for vertex, path in visit.items():
                path.distance *= multitude_of

    def add_vertex(self, vertex):
        self.graph[vertex] = {}
        print("New location added successfully.")

    def delete_vertex(self, vertex_name):
        vertex_to_delete = self.find_vertex(vertex_name)

        if vertex_to_delete is None:
            print(f"Location '{vertex_name}' not found.")
            return
        if vertex_to_delete in self.graph:
            del self.graph[vertex_to_delete]
            # print(f"Deleted vertex: {vertex_to_delete.name}")
        for start, adjacencies in list(self.graph.items()):
            if vertex_to_delete in adjacencies:
                del adjacencies[vertex_to_delete]
                # print(f"Removed edge from {start.name} to {vertex_to_delete.name}")
        print("\nLocation deleted successfully.")

    def find_vertex(self, vertex_name):
        for vertex in self.graph:
            if (vertex.name.lower() == vertex_name.lower()):
                # print("Found vertex.")
                return vertex
        # print("Vertex not found.")
        return None

    def add_edge(self, vertex1_name, vertex2_name, edge):
        vertex1 = self.find_vertex(vertex1_name)
        vertex2 = self.find_vertex(vertex2_name)

        if not vertex1 or not vertex2:
            raise ValueError(f"One or both location '{vertex1_name}' and '{vertex2_name}' not found in the graph!")

        if vertex1 not in self.graph:
            self.graph[vertex1] = {}
        self.graph[vertex1][vertex2] = edge

        self.graph[vertex1][vertex2].set_distance((math.sqrt(pow(abs(vertex1.x - vertex2.x), 2) + pow(abs(vertex1.y - vertex2.y), 2))) * self.scale)
        print("\nNew path added successfully.")

    def get_valid_input(self, prompt_type, prompt, choices=None):
        while True:
            try:
                if prompt_type == "int":
                    user_input = int(input(prompt))
                elif prompt_type == "string":
                    user_input = input(prompt).strip()
                elif prompt_type == "float":
                    user_input = float(input(prompt))
                elif prompt_type == "boolean":
                    user_input = input(prompt)
                else:
                    print(f"Error: Unsupported prompt type '{prompt_type}'. Please use 'int', 'string', or 'float'.")
                    return None

                if choices:
                    if isinstance(choices, tuple) and len(choices) == 2 and prompt_type == "float":
                        # Check if the float input is within the range
                        if choices[0] <= user_input <= choices[1]:
                            return user_input
                        else:
                            print(f"Error: {user_input} is not in the valid range {choices[0]} to {choices[1]}.")
                    elif prompt_type == "string" and isinstance(choices, set):
                        # For case-insensitive string matching
                        if user_input.lower() in {str(choice).lower() for choice in choices}:
                            return next(choice for choice in choices if str(choice).lower() == user_input.lower())
                        else:
                            print(f"Error: '{user_input}' is not a valid choice. Please choose from {choices}.")
                    elif prompt_type == "boolean" :
                        # For case-insensitive string matching
                        if user_input.lower() == "true": return True
                        elif user_input.lower() == "false": return False
                        else: print(f"Error: '{user_input}' is not a valid choice. Please choose either true or false.")
                    elif prompt_type == "int":
                        # For other types (int or exact match)
                        if user_input in choices:
                            return user_input
                        else:
                            print(f"Error: {user_input} is not a valid choice. Please choose from {choices}.")
                else:
                    # No restrictions
                    return user_input

            except ValueError:
                print(f"Error: Invalid input type. Expected a {prompt_type}. Please try again.")

    def edit_path(self, roadName, change):
        for start, end in self.graph.items():
            for key, value in end.items():
                if value.road_name.lower() == roadName.lower():
                    if change == 1:
                       value.road_name = self.get_valid_input("string", "Please enter the correct road name: ")
                       print("\nRoad information updated successfully.")
                    elif change == 2:
                        print("Tipe dari jalan: \n'1 : Jalan biasa', '2 : Jalan Tol', '3 : Jalan sempit/gang', '4 : Jalan pejalan kaki'.")
                        value.road_type = self.get_valid_input("int", "Please enter the current road type: ", {1, 2, 3, 4})
                        print("\nRoad information updated successfully.")
                    elif change == 3:
                        print("Kondisi dari jalan: 'True : Bagus', 'False : Buruk'.")
                        value.road_condition = self.get_valid_input("boolean", "Please enter the current road condition: ", {"true", "false"})
                        print("\nRoad information updated successfully.")
                    elif change == 4:
                        print("Tingkat kemacetan antara range 0.0 (Sangat lancar) - 1.0 (Macet Total)")
                        value.road_congestion = self.get_valid_input("float", "Please enter the current road congestion rate:", (0.0, 1.0))
                        print("\nRoad information updated successfully.")
                    else :
                        print("Input outside of choices. Please try again.")
                    return

        print("Sorry, we don't seem to have a road with that name.")

    # hitung final_time edge dgn mempertimbangakn kemacetan, jalan, speed, jam brngkt.
    def calculate_edge(self, path, vehicle, curr_time=Timer()):
        base_time= path.travel_time(vehicle.speed) #waktu dasar dr jarak/kecepatan

        if curr_time:
            hour, minute, second = curr_time.get_time()
            # jam 7.00 - 9.00 atau jam 16.00 - 18.00
            if (7 <= hour <= 9) or (16 <= hour <= 18):
                path.congestion= min(path.congestion + (1 - path.congestion) * 0.3, 1.0)  #menambah kemacetan
            # off hours 22.00 - 05.00
            elif (22 <= hour <= 23) or (0 <= hour <= 5):
                path.congestion= max(path.congestion - path.congestion * 0.2, 0.0)  #mengurangi kemacetan
            else:
                path.congestion= path.congestion  #normal

         # Menghitung waktu final dengan mempertimbangkan kemacetan dan kondisi jalan
        final_time = base_time / (1 - path.congestion) if path.congestion != 1 else 9999

        if not path.condition: #kalo jalan buruk dikalikan 1.5
            final_time *= 1.5

        return final_time


    def shortest_times(self, source, vehicle, start_time = Timer()):
        # Dijkstra Algorithm
        # Initialize the values of all nodes with infinity
        distances = {vertex: {'jarak' : float("inf"), 'waktu' : float("inf")} for vertex in self.graph}
        distances[source]['jarak'] = 0  # Set the source value to 0
        distances[source]['waktu'] = start_time.get_hours()

        # Initialize priority queue
        pq = [(0, 0, source)] # [(time satuan jam, distance satuan m, vertex)] priority queue nya berdasarkan time terkecil.
        heapify(pq)

        # Set to hold visited nodes
        visited = set()

        while pq:
            current_time, current_distance, current_vertex = heappop(pq)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbour_vertex, neighbour_path in self.graph[current_vertex].items():
                # Calculate the distance from current_vertex to the neighbour_vertex
                # Ini skrg aku tambahin supaya cuma jenis kendaraan tertentu yang bisa lewat jalan tertentu
                if vehicle.can_traverse(neighbour_path.road_type):
                    neighbour_time_weight = neighbour_path.travel_time(vehicle.speed)  # Format: x Jam
                  # neighbour_time_weight = self.calculate_edge(neighbour_path, vehicle, start_time) # Format: x Jam

                    tentative_distance = current_distance + neighbour_path.distance
                    tentative_time = current_time + neighbour_time_weight
                    if tentative_time < distances[neighbour_vertex]['waktu']:
                        distances[neighbour_vertex]['jarak'] = tentative_distance

                        #hitung  arrival time di neighbour
                        distances[neighbour_vertex]['waktu'] = tentative_time

                        heappush(pq, (tentative_time, tentative_distance, neighbour_vertex))

        # Melihat Jalur awalnya
        predecessors = {vertex: {'vertex_asal' : None, 'path' : None} for vertex in self.graph}
        for vertex, distance in distances.items():
            for neighbour_vertex, neighbour_path in self.graph[vertex].items():
                if (distance['jarak'] + neighbour_path.distance == distances[neighbour_vertex]['jarak']
                        and distances[neighbour_vertex]['jarak'] != float('inf') and vehicle.can_traverse(neighbour_path.road_type)):
                    predecessors[neighbour_vertex]['vertex_asal'] = vertex
                    predecessors[neighbour_vertex]['path'] = neighbour_path

        return distances, predecessors

    def shortest_distances(self, source, vehicle, start_time = Timer()): # Jalan alternatif yang jarak terbendek, bukan waktu tersingkat
        # Dijkstra Algorithm
        # Initialize the values of all nodes with infinity
        distances = {vertex: {'jarak' : float("inf"), 'waktu' : float("inf")} for vertex in self.graph}
        distances[source]['jarak'] = 0  # Set the source value to 0
        distances[source]['waktu'] = start_time.get_hours()

        # Initialize priority queue
        pq = [(0, 0, source)] # [(time satuan jam, distance satuan km, vertex)] priority queue nya berdasarkan time terkecil.
        heapify(pq)

        # Set to hold visited nodes
        visited = set()

        while pq:
            current_distance, current_time, current_vertex = heappop(pq)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbour_vertex, neighbour_path in self.graph[current_vertex].items():
                # Calculate the distance from current_vertex to the neighbour_vertex
                # Ini skrg aku tambahin supaya cuma jenis kendaraan tertentu yang bisa lewat jalan tertentu
                if vehicle.can_traverse(neighbour_path.road_type):
                    neighbour_time_weight = neighbour_path.travel_time(vehicle.speed)  # Format: x Jam
                  # neighbour_time_weight = self.calculate_edge(neighbour_path, vehicle, start_time) # Format: x Jam

                    tentative_distance = current_distance + neighbour_path.distance
                    tentative_time = current_time + neighbour_time_weight
                    if tentative_distance < distances[neighbour_vertex]['jarak']:
                        distances[neighbour_vertex]['jarak'] = tentative_distance

                        #hitung  arrival time di neighbour
                        distances[neighbour_vertex]['waktu'] = tentative_time

                        heappush(pq, (tentative_distance, tentative_time, neighbour_vertex))

        # Melihat Jalur awalnya
        predecessors = {vertex: {'vertex_asal' : None, 'path' : None} for vertex in self.graph}
        for vertex, distance in distances.items():
            for neighbour_vertex, neighbour_path in self.graph[vertex].items():
                if (distance['jarak'] + neighbour_path.distance == distances[neighbour_vertex]['jarak']
                        and distances[neighbour_vertex]['jarak'] != float('inf') and vehicle.can_traverse(neighbour_path.road_type)):
                    predecessors[neighbour_vertex]['vertex_asal'] = vertex
                    predecessors[neighbour_vertex]['path'] = neighbour_path

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
                    else:return "Belok Kanan Ke" #Kanan Kanan / Kiri Kanan
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


    def go_from_a_to_b_waktu_tercepat(self, source, destination, vehicle, start_time = Timer()):
        if type(source) == str and type(destination) == str:  # Cek source & destination apakah ada di graph
            sourceKetemu = False
            destinationKetemu = False
            for vertex in self.graph:
                if not sourceKetemu and vertex.name.lower() == source.lower():
                    source = vertex
                    sourceKetemu = True
                if not destinationKetemu and vertex.name.lower() == destination.lower():
                    destination = vertex
                    destinationKetemu = True
            if not sourceKetemu or not destinationKetemu:
                if not sourceKetemu: print("Source tidak ditemukan!")
                if not destinationKetemu: print("Destination tidak ditemukan!")

        print("===JALUR BERDASARKAN WAKTU TERCEPAT===")

        distances, predecessors = self.shortest_times(source, vehicle, start_time)

        if (distances[destination] == float('inf')):
            print(f"no valid path from {source.name} to {destination.name}")
            return

        # Hitung waktu kedatangan
        arrival_times = {}  # Dictionary untuk waktu kedatangan
        for node, distance in distances.items():
            if start_time and distance['waktu'] != float('inf'):
                arrival_times[node] = start_time.get_hours() + distance['waktu']

        # print start dan estimated time
        str_start_time = start_time.get_time_formatted() if start_time else "now"
        arrival_time = Timer(hours=arrival_times[destination]) if destination in arrival_times else None
        total_time = Timer(hours=distances[destination]['waktu']) #dalam menit
        hours, minutes, seconds = total_time.get_time()


        print(f"\nStart time: {str_start_time}")
        print(f"Estimated arrival time: {arrival_time.get_time_formatted() if arrival_time else 'unknown'}")
        if hours == 0 and minutes == 0: # Kurang yakin ini fungsinya apa
            minutes = 1
        if hours > 0:
            print(f"Total travel time: {hours} hours {minutes} minutes")
        else:
            print(f"Total travel time: {minutes} minutes")


        trace = []
        current_vertex = destination
        total_distance = 0

        while predecessors[current_vertex]['path'] is not None:
            total_distance += predecessors[current_vertex]['path'].distance
            trace.append(predecessors[current_vertex])
            current_vertex = predecessors[current_vertex]['vertex_asal']

        trace.reverse()
        direction = True

        for i in range(len(trace)):
            direction = False
            if (i > 0 and trace[i]['path'].road_name == trace[i-1]['path'].road_name):
                print("Lurus Ke", end = " ")
                direction = True

            if (not direction):
                if (i > 0):
                    if (i+1 == len(trace)):
                        print(self.getNextDirection(trace[i - 1]['vertex_asal'], trace[i]['vertex_asal'], destination), end = " ")
                    elif (i+1 < len(trace)):
                        print(self.getNextDirection(trace[i - 1]['vertex_asal'], trace[i]['vertex_asal'], trace[i+1]['vertex_asal']), end = " ")

                else:
                    if (i+1 == len(trace)):
                        print(self.getFirstDirection(trace[i]['vertex_asal'], destination), end = " ")
                    else:
                        print(self.getFirstDirection(trace[i]['vertex_asal'], trace[i+1]['vertex_asal']), end = " ")

            # print(instruction[i] if instruction[i] else None, end = " ")
            print(trace[i]['path'].road_name if trace[i]['path'] else None)

            # Hitung jarak per jalan
            jarak = round(trace[i]['path'].distance)
            print("Ikuti jalan sejauh", str(jarak) + " M" if jarak < 1000 else str(jarak/1000) + " KM")
        print("\nAnda Telah Tiba Di Tujuan Anda!")

        if vehicle.speed <= 0:
            print("must greater then zero!")
        else:
            time_taken = total_distance / vehicle.speed
            #Fuel Efficiency = ... KM / liter
            #Karena total_distance mainly M kita ubah ke KM dulu trus bagi dengan fuel efficiency buat dapet
            #Konsumsinya berapa banyak
        fuel_consumed = (total_distance / 1000) / vehicle.fuel_efficiency

        if(total_distance >= 1000):
            print(f"\nTotal jarak: {round(total_distance) / 1000} KM")
        else:
            print(f"\nTotal jarak: {total_distance} M")

        if (fuel_consumed >= 1):
            print(f"Konsumsi bahan bakar: {fuel_consumed:.2f} Liter")
        else:
            print(f"Konsumsi bahan bakar: {fuel_consumed * 1000} mL")


    def go_from_a_to_b_jarak_terdekat(self, source, destination, vehicle, start_time = Timer()):
        if type(source) == str and type(destination) == str:  # Cek source & destination apakah ada di graph
            sourceKetemu = False
            destinationKetemu = False
            for vertex in self.graph:
                if not sourceKetemu and vertex.name.lower() == source.lower():
                    source = vertex
                    sourceKetemu = True
                if not destinationKetemu and vertex.name.lower() == destination.lower():
                    destination = vertex
                    destinationKetemu = True
            if not sourceKetemu or not destinationKetemu:
                if not sourceKetemu: print("Source tidak ditemukan!")
                if not destinationKetemu: print("Destination tidak ditemukan!")

        distances2, predecessors2 = self.shortest_distances(source, vehicle, start_time)

        print("===JALUR BERDASARKAN JARAK TERDEKAT===")

        if (distances2[destination] == float('inf')):
            print(f"no valid path from {source.name} to {destination.name}")
            return

        # Hitung waktu kedatangan
        arrival_times = {}  # Dictionary untuk waktu kedatangan
        for node, distance in distances2.items():
            if start_time and distance['waktu'] != float('inf'):
                arrival_times[node] = start_time.get_hours() + distance['waktu']

        # print start dan estimated time
        str_start_time = start_time.get_time_formatted() if start_time else "now"
        arrival_time = Timer(hours=arrival_times[destination]) if destination in arrival_times else None
        total_time = Timer(hours=distances2[destination]['waktu'])  # dalam menit
        hours, minutes, seconds = total_time.get_time()

        print(f"\nStart time: {str_start_time}")
        print(f"Estimated arrival time: {arrival_time.get_time_formatted() if arrival_time else 'unknown'}")
        if hours == 0 and minutes == 0:  # Kurang yakin ini fungsinya apa
            minutes = 1
        if hours > 0:
            print(f"Total travel time: {hours} hours {minutes} minutes")
        else:
            print(f"Total travel time: {minutes} minutes")

        trace = []
        current_vertex = destination
        total_distance = 0

        while predecessors2[current_vertex]['path'] is not None:
            total_distance += predecessors2[current_vertex]['path'].distance
            trace.append(predecessors2[current_vertex])
            current_vertex = predecessors2[current_vertex]['vertex_asal']

        trace.reverse()
        direction = True

        for i in range(len(trace)):
            direction = False
            if (i > 0 and trace[i]['path'].road_name == trace[i - 1]['path'].road_name):
                print("Lurus Ke", end=" ")
                direction = True

            if (not direction):
                if (i > 0):
                    if (i + 1 == len(trace)):
                        print(self.getNextDirection(trace[i - 1]['vertex_asal'], trace[i]['vertex_asal'], destination),
                              end=" ")
                    elif (i + 1 < len(trace)):
                        print(self.getNextDirection(trace[i - 1]['vertex_asal'], trace[i]['vertex_asal'],
                                                    trace[i + 1]['vertex_asal']), end=" ")

                else:
                    if (i + 1 == len(trace)):
                        print(self.getFirstDirection(trace[i]['vertex_asal'], destination), end=" ")
                    else:
                        print(self.getFirstDirection(trace[i]['vertex_asal'], trace[i + 1]['vertex_asal']), end=" ")

            # print(instruction[i] if instruction[i] else None, end = " ")
            print(trace[i]['path'].road_name if trace[i]['path'] else None)

            # Hitung jarak per jalan
            jarak = round(trace[i]['path'].distance)
            print("Ikuti jalan sejauh", str(jarak) + " M" if jarak < 1000 else str(jarak / 1000) + " KM")
        print("\nAnda Telah Tiba Di Tujuan Anda!")

        if vehicle.speed <= 0:
            print("must greater then zero!")
        else:
            time_taken = total_distance / vehicle.speed
        fuel_consumed = (total_distance / 1000) / vehicle.fuel_efficiency

        if (total_distance >= 1000):
            print(f"\nTotal jarak: {round(total_distance) / 1000} KM")
        else:
            print(f"\nTotal jarak: {total_distance} M")

        if (fuel_consumed >= 1):
            print(f"Konsumsi bahan bakar: {fuel_consumed:.2f} Liter")
        else:
            print(f"Konsumsi bahan bakar: {fuel_consumed * 1000:.0f} mL")


    def print_graph(self):
        for start, end in self.graph.items():
            for key, value in end.items():
                print(f"{start.name}, {key.name}, distance:{value.distance} M, road_name:{value.road_name}, road_type:{value.road_type}, condition:{value.condition}, congestion:{value.congestion}")

    def list_of_locations(self):
        edges = set()
        for start, end in self.graph.items():
            if start.name not in edges:
                edges.add(start.name)

            for key in end.keys():
                if key.name not in edges:
                    edges.add(key.name)
        return edges

