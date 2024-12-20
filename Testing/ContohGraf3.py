from Car import Car
from Graph import Graph
from Motorcycle import Motorcycle
from Path import Path
from Timer import Timer
from Vertex import Vertex

Start = Vertex(0, 3, "Start")
A = Vertex(3, 0, "A")
B = Vertex(4, 3, "B", True)
C = Vertex(4, 6, "C")
D = Vertex(6, -1, "D")
E = Vertex(10, -1, "E")
F = Vertex(13, 0, "F")
End = Vertex(16, 3, "End")
G = Vertex(13, 6, "G")
H = Vertex(13, 3, "H", True)

pathSA = Path("Jalan Tol Satelit1", 2, True, 0)
pathAD = Path("Jalan Tol Satelit2", 2, True, 0)
pathDE = Path("Jalan Tol Satelit3", 2, True, 0)
pathEF = Path("Jalan Tol Satelit4", 2, True, 0)
pathFEnd = Path("Jalan Tol Satelit5", 2, True, 0)

pathSB = Path("Jalan Ayani", 1, True, 0)
pathBS = Path("Jalan Ayani", 1, True, 0)
pathBC = Path("Jalan Ayani", 1, True, 0)
pathCB = Path("Jalan Ayani", 1, True, 0)
pathBH = Path("Jalan Ayani", 1, True, 0)
pathHB = Path("Jalan Ayani", 1, True, 0)
pathHG = Path("Jalan Ayani", 1, True, 0)
pathGH = Path("Jalan Ayani", 1, True, 0)
pathHEnd = Path("Jalan Ayani", 1, True, 0)
pathEndH = Path("Jalan Ayani", 1, True, 0)

pathSC = Path("Jalan Desa", 1, True, 0)
pathCG = Path("Jalan Gang Sempit", 3, True, 0)
pathGEnd = Path("Jalan Desa", 1, True, 0)

contoh_graph3 = {
    Start: {A: pathSA, B: pathSB, C: pathSC},
    A: {D: pathAD},
    B: {Start: pathBS,H: pathBH, C: pathBC},
    C: {G: pathCG, B: pathCB},
    D: {E: pathDE},
    E: {F: pathEF},
    F: {End: pathFEnd},
    End: {H: pathEndH},
    G: {End: pathGEnd, H: pathGH},
    H: {B: pathHB, End: pathHEnd, G: pathHG}
}
gr = Graph(1000)
gr.make_graph(contoh_graph3)

distances, predecessors = gr.shortest_times(Start, Car(50, 50), Timer(hours=9, minutes=30))
print("===DISTANCES===")
for key, value in distances.items():
    print(f"{key.name}: [{value['jarak']}, {Timer(hours=value['waktu'])}]", end = " M\n")

print("===PREDECESSOR===")
for key, value in predecessors.items():
    print(f"{key.name}: {value['vertex_asal'].name if value['vertex_asal'] else None} {value['path'].road_name if value['path'] else None}")
#
# gr.go_from_a_to_b_waktu_tercepat(Start, End, Car(50, 10), Timer(9, 30))
# gr.go_from_a_to_b_jarak_terdekat(Start, End, Car(50, 10), Timer(9, 30))

gr.go_from_a_to_b_waktu_tercepat(Start, End, Motorcycle(50, 10), Timer(9, 30))
gr.go_from_a_to_b_jarak_terdekat(Start, End, Motorcycle(50, 10), Timer(9, 30))