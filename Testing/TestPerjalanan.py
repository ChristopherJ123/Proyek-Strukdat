predecessors = {'A': None, 'B': 'A', 'C': 'A', 'D': 'A', 'E': 'B', 'F': 'E', 'G': 'C', 'H': 'F'}
destination = ['H']

while predecessors[destination[-1]] is not None:
    print(destination)
    print("destination[-1] is " + destination[-1])
    print("predecessors[destination[-1]] is " + str(predecessors[destination[-1]]))
    print("---")
    destination.append(predecessors[destination[-1]])
    # print(dict1[destination[-1]])
    # print("---")

print(destination)
destination.reverse()

print("===")
print(destination)
print("===")

print("Dari ", end="")
print(" pergi ke ".join(destination))
