from Graph import Graph
from Path import Path
from Vertex import Vertex
from Walking import Walking
from Car import Car
from Motorcycle import Motorcycle

gr = Graph()
car = Car(50, 10)
motor = Motorcycle(40, 10)

A = Vertex(0, 0, "A")
B = Vertex(3, 4, "B")
C = Vertex(5, -5, "C")
D = Vertex(5, 1, "D")
E = Vertex(12, 0, "E")
F = Vertex(8, -5, "F")
G = Vertex(9, 4, "G")
H = Vertex(8, -2, "H")
I = Vertex(0, -5, "I")

pathAB = Path("Jl. Alfa Bravo", 1, True, 0.0)
pathAC = Path("Jl. Alfa Charlie", 1, True, 0.0)
pathAD = Path("Jl. Alfa Delta", 1, True, 0.0)
pathAI = Path("Jl. Alfa India", 3, True, 0.0)

pathBG = Path("Jl. Bravo Golf", 1, True, 0.0)

pathCF = Path("Jl. Charlie Foxtrot", 1, True, 0.0)
pathCI = Path("Jl. Charlie India", 1, True, 0.0)


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
    A : {B : pathAB, C : pathAC, D : pathAD, I : pathAI},
    B : {G : pathBG},
    C : {F : pathCF, I : pathCI},
    D : {G : pathDG, H : pathDH},
    E : {},
    F : {E : pathFE},
    G : {E : pathGE},
    H : {C : pathHC, E : pathHE},
    I : {}
}

gr.make_graph(graph)
# gr.print_graph()
distances, predecessor = gr.shortest_distances(A, car)
# print(f"distances: {distances}")
# print(f"predecessor: {predecessor}")

print("===DISTANCES===")
for key, value in distances.items():
    print(f"{key.name}: {value} KM")



print("===PREDECESSOR===")

for key, value in predecessor.items():
    print(f"{key.name}: {value[0].name if value[0] else None} {value[1].road_name if value[1] else None}")


print("Pergi dari A ke F:")
gr.go_from_a_to_b(A, I, car)

print()
distances2, predecessor2 = gr.shortest_distances(A, motor)


print("===DISTANCES 2===")
for key, value in distances2.items():
    print(f"{key.name}: {value} KM")

print("===PREDECESSOR 2===")

for key, value in predecessor2.items():
    print(f"{key.name}: {value[0].name if value[0] else None} {value[1].road_name if value[1] else None}")

print("Pergi dari A ke F 2:")
gr.go_from_a_to_b(A, I, motor)


# format
# DijkstraAlgorithmOld
# {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf}
# {'A': 0, 'B': 4, 'C': 3, 'D': 5, 'E': 7, 'F': 8, 'G': 9, 'H': 17} {'A': None, 'B': 'A', 'C': 'A', 'D': 'A', 'E': 'B', 'F': 'E', 'G': 'C', 'H': 'F'}
# Now:
# {<Vertex.Vertex object at 0x000001C1026E2450>: 0, <Vertex.Vertex object at 0x000001C1026E2090>: 5.0, <Vertex.Vertex object at 0x000001C1026E20D0>: 7.0710678118654755, <Vertex.Vertex object at 0x000001C1042D0910>: 5.0990195135927845, <Vertex.Vertex object at 0x000001C1042D0950>: 13.81379615571165, <Vertex.Vertex object at 0x000001C1042D0B10>: 10.071067811865476, <Vertex.Vertex object at 0x000001C1042D0B50>: 10.099019513592784, <Vertex.Vertex object at 0x000001C1042D0B90>: 9.34166020071207}
# {<Vertex.Vertex object at 0x000001C1026E2450>: None, <Vertex.Vertex object at 0x000001C1026E2090>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1026E20D0>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1042D0910>: <Vertex.Vertex object at 0x000001C1026E2450>, <Vertex.Vertex object at 0x000001C1042D0950>: <Vertex.Vertex object at 0x000001C1042D0B90>, <Vertex.Vertex object at 0x000001C1042D0B10>: <Vertex.Vertex object at 0x000001C1026E20D0>, <Vertex.Vertex object at 0x000001C1042D0B50>: <Vertex.Vertex object at 0x000001C1042D0910>, <Vertex.Vertex object at 0x000001C1042D0B90>: <Vertex.Vertex object at 0x000001C1042D0910>}

#coba coba:
print()
print("coba coba")

graf = Graph()
a = Vertex(0, 0, "a")
b = Vertex(0, 5, "b")
c = Vertex(-10, 5, "c")
d = Vertex(10, 5, "d")

pathab = Path("Jl. Alfa Bravo", 1, True, 0.0)
pathbc = Path("Jl. Alfa Charlie", 1, True, 0.0)
pathbd = Path("Jl. Alfa Delta", 1, True, 0.0)

graphh = {
    a : {b : pathab},
    b : {a : pathab, c : pathbc, d : pathbd},
    c : {b : pathbc},
    d : {b : pathbd},
}
graf.make_graph(graphh)
jarak, predesesor = graf.shortest_distances(a, car)

print("===DISTANCES===")
for key, value in jarak.items():
    print(f"{key.name}: {value} KM")



print("===PREDECESSOR===")

for key, value in predesesor.items():
    print(f"{key.name}: {value[0].name if value[0] else None} {value[1].road_name if value[1] else None}")

#Arah kiri kanannya masih blm bener
print("Pergi dari A ke C:")
graf.go_from_a_to_b(a, c, car)
print()
print("Pergi dari A ke D:")
graf.go_from_a_to_b(a, d, car)


def print_mainPage():
    print("\n================== Main Page ==================")
    print("Choices : ")
    print("1. Edit map")
    print("2. Search for shortest distance")
    print("3. Display map")
    print("0. Exit")

def print_mapPage():
    print("\n=============== Map Editor Page ===============")
    print("Choices : ")
    print("1. Add new location") 
    print("2. Delete existing location")
    print("3. Add new road")
    print("4. Update road information")
    print("0. Exit")
    print("-1. Back to the main page")

def createPath():
    road_name = input("\nWhat is the name of the road? ")
    print("Tipe dari jalan: \n'1 : Jalan biasa', '2 : Jalan Tol', '3 : Jalan sempit/gang', '4 : Jalan pejalan kaki'.")
    road_type = int(input("Input road type: "))
    print("Kondisi dari jalan: 'True : Bagus', 'False : Buruk'.")
    road_condition = bool(input("Input road condition: "))
    print("Tingkat kemacetan antara range 0.0 (Sangat lancar) - 1.0 (Macet Total)")
    road_congestion = float(input("Input road congestion rate: "))
    return Path(road_name, road_type, road_condition, road_congestion)


choice = 1
while choice!=0:
    print_mainPage()
    choice = int(input("Please enter your choice here: "))

    if choice == 1 :
        while choice == 1 :
            print_mapPage()
            input2 = int(input("Please enter your choice here: "))
            if input2 == 1:
                print("\nTo add a new location, please input the following details.")
                vertex_name = input("Location name: ")
                x = int(input("X-coordinates of the location: "))
                y = int(input("Y-coordinates of the location: "))

                vertex_new = Vertex(x, y, vertex_name) 
                gr.add_vertex(vertex_new)

            elif input2 == 2:
                print("\nTo delete an existing location, please input the following details.")
                vertex_name = input("Location name: ")
                gr.delete_vertex(vertex_name)

            elif input2 == 3:
                print("\nTo create a new path, please input the following details.")
                start = input("Where is the starting point of the path? ")
                end = input("To where does the path lead to? ")
                pathXX = createPath()

                gr.add_edge(start, end, pathXX)

            elif input2 == 4:
                print("\nTo update road information, please input the following details.")
                road_name = input("What is the name of the road? ")
                print("Of the following details, which one would you like to change?\n1. Road Name\n2. Road Type\n3. Road Condition\n4. Road Congestion Rate")
                road_update = int(input("Please enter your choice here (You may only choose one):  "))

                gr.edit_path(road_name, road_update)

            elif input2 == 0:
                choice = 0
                print("\nExiting...")
                break
            elif input2 == -1:
                choice = -1
                print("\nGoing back into the main page...")
            else :
                print("Input outside of choices. Please try again.")


    elif choice == 2:
        start = input("\nWhere do you want to start your journey? ")
        end = input("Where do you want to go? ")
        gr.go_from_a_to_b(start, end, car)


    elif choice == 3:
        print("\nHere is the current map: ")
        gr.print_graph()

    elif choice == 0:
        choice = 0
        print("\nExiting...")
        break
    else :
        print("Input outside of choices. Please try again.")
    

