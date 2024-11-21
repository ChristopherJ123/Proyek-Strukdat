dict1 = {'A': None, 'B': 'A', 'C': 'A', 'D': 'A', 'E': 'B', 'F': 'E', 'G': 'C', 'H': 'F'}
destination = ['H']

while dict1[destination[-1]] is not None:
    print("dict1[destination[-1]] is " + str(dict1[destination[-1]]))
    destination.append(dict1[destination[-1]])
destination.reverse()

print(destination)