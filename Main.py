from Car import Car
from Bus import Bus
from Bicycle import Bicycle
from Walking import Walking
from Graph import Graph
from Motorcycle import Motorcycle
from Path import Path
from Timer import Timer
from Vertex import Vertex

car = Car(50, 10) #Pemakaian 10 KM / Liter

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

graph = {
    A : {B : pathAB, C : pathAC, D : pathAD},
    B : {G : pathBG},
    C : {F : pathCF},
    D : {G : pathDG, H : pathDH},
    E : {},
    F : {E : pathFE},
    G : {E : pathGE},
    H : {C : pathHC, E : pathHE},
}

gr = Graph()
gr.make_graph(graph)
gr.scale_distances(1000)

def print_mainPage(): #Evelyn
    print("\n================== Main Page ==================")
    print("Choices: ")
    print("1. Edit map")
    print("2. Search for optimal path")
    print("3. Display map")
    print("0. Exit")

def print_optimalPathPage(): #Evelyn
    print("\n============== Optimal Path Page ==============")
    print("Start point: ", start)
    print("Destination point: ", end)
    print("Current vehicle: ", current_vehicle.vehicle_type)
    print("Choices: ")
    print("> Search for optimal path based on: ")
    print("1. The shortest distance") 
    print("2. The shortest amount of estimated time")
    print("> Or do the following: ")
    print("3. Change start point")
    print("4. Change destination point")
    print("5. Change current vehicle")
    print("0. Exit")
    print("-1. Back to the main page")

def print_mapPage(): #Evelyn
    print("\n=============== Map Editor Page ===============")
    print("Choices: ")
    print("1. Add new location") 
    print("2. Delete existing location")
    print("3. Add new road")
    print("4. Update road information")
    print("5. Display map")
    print("0. Exit")
    print("-1. Back to the main page")

def createPath(): #Evelyn
    road_name = get_valid_input("string", "\nWhat is the name of the road? ")

    print("Tipe dari jalan: \n'1 : Jalan biasa', '2 : Jalan Tol', '3 : Jalan sempit/gang', '4 : Jalan pejalan kaki'.")
    valid_choices = {1, 2, 3, 4}
    road_type = get_valid_input("int", "Input road type: ", valid_choices)

    print("Kondisi dari jalan: 'True : Bagus', 'False : Buruk'.")
    road_condition = get_valid_input("boolean", "Input road condition: ", {"true", "false"})

    print("Tingkat kemacetan antara range 0.0 (Sangat lancar) - 1.0 (Macet Total)")
    valid_choices = (0.0, 1.0)
    road_congestion = get_valid_input("float", "Input road congestion rate: ", valid_choices)

    return Path(road_name, road_type, road_condition, road_congestion)


def get_valid_input(prompt_type, prompt, choices=None): #Evelyn
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


choice = 1
prompt1 = "Please enter your choice here: "
current_vehicle = car
bus = Bus(45, 12)
walking = Walking(5) #km/jam
bicycle = Bicycle(24)
car = Car(50, 10) #Pemakaian 10 KM / Liter
motorcycle = Motorcycle(60, 10) #Pemakaian 10 KM / Liter


while choice!=0:
    print_mainPage()
    choice = get_valid_input("int", prompt1, {1, 2, 3, 0})

    if choice == 1 :
        while choice == 1 :
            print_mapPage()
            input1 = get_valid_input("int", prompt1, {1, 2, 3, 4, 5, 0, -1})
            print()
            
            if input1 == 1:
                print("To add a new location, please input the following details.")
                vertex_name = input("Location name: ")
                x = get_valid_input("int", "X-coordinates of the location: ")
                y = get_valid_input("int", "Y-coordinates of the location: ")

                vertex_new = Vertex(x, y, vertex_name) 
                gr.add_vertex(vertex_new)

            elif input1 == 2:
                print("To delete an existing location, please input the following details.")
                vertex_name = get_valid_input("string", "Location name: ")
                gr.delete_vertex(vertex_name)

            elif input1 == 3:
                print("To create a new path, please input the following details.")
                vertexes = gr.list_of_locations()
                start = get_valid_input("string", "Where is the starting point of the path? ", vertexes)
                end = get_valid_input("string", "To where does the path lead to? ", vertexes)
                pathXX = createPath()

                gr.add_edge(start, end, pathXX)

            elif input1 == 4:
                print("To update road information, please input the following details.")
                road_name = get_valid_input("string", "What is the name of the road? ")
                print("Of the following details, which one would you like to change?\n1. Road Name\n2. Road Type\n3. Road Condition\n4. Road Congestion Rate")
                road_update = get_valid_input("int", "Please enter your choice here (You may only choose one):  ", {1, 2, 3, 4})

                gr.edit_path(road_name, road_update)
                
            elif input1 == 5:
                print("Here is the current map: ")
                gr.print_graph()

            elif input1 == 0:
                choice = 0
                print("Exiting...")
                break
            elif input1 == -1:
                choice = -1
                print("Going back into the main page...")
            else :
                print("Input outside of choices. Please try again.")

    elif choice == 2:
        vertexes = gr.list_of_locations()
        start = get_valid_input("string", "\nWhere do you want to start your journey? ", vertexes)
        end = get_valid_input("string", "Where do you want to go? ", vertexes)

        while choice == 2 :
            print_optimalPathPage()
            input2 = get_valid_input("int", prompt1, {1, 2, 3, 4, 5, 0, -1})
            print()
            if input2 == 1:
                gr.go_from_a_to_b_jarak_terdekat(start, end, current_vehicle)

            elif input2 == 2:
                gr.go_from_a_to_b_waktu_tercepat(start, end, current_vehicle)
            
            elif input2 == 3:
                start = get_valid_input("string", "Where do you want to start your journey? ", vertexes)

            elif input2 == 4:
                end = get_valid_input("string", "Where do you want to go? ", vertexes)

            elif input2 == 5:
                print(f"Your current vehicle is a {current_vehicle.vehicle_type}. What would you like to change it into?")
                print("The choices are : Car, Motorcycle, Bus, Bicycle, Walking")
                vehicle_list = {"Car", "Motorcycle", "Bus", "Bicycle", "Walking"}
                inp_vehicle = get_valid_input("string", prompt1, vehicle_list)

                if inp_vehicle.lower() == "car":
                    current_vehicle = car
                elif inp_vehicle.lower() == "motorcycle":
                    current_vehicle = motorcycle
                elif inp_vehicle.lower() == "bus":
                    current_vehicle = bus
                elif inp_vehicle.lower() == "bicycle":
                    current_vehicle = bicycle
                elif inp_vehicle.lower() == "walking":
                    pcurrent_vehicle = walking
                else:
                    print("Invalid choice. Please select from the provided options.")

            elif input2 == 0:
                choice = 0
                print("Exiting...")
                break
            elif input2 == -1:
                choice = -1
                print("Going back into the main page...")
            else :
                print("Input outside of choices. Please try again.")
        
        
    elif choice == 3:
        print("\nHere is the current map: ")
        gr.print_graph()

    elif choice == 0:
        choice = 0
        print("\nExiting...")
        break
    # elif choice == -1
    #     print()
    # else :
    #     print("Input outside of choices. Please try again.")
    
