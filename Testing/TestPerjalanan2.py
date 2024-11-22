dict1 = {
    'A': [None, None],
    'B': ['A', 'Jl. AB'],
    'C': ['A', 'Jl.AC'],
    'D': ['A', 'Jl.AD'],
    'E': ['B', 'Jl. Echo Bravo'],
    'F': ['E', 'Jl. Foxtrot Echo'],
    'G': ['C', 'Jl. Golf Charlie'],
    'H': ['F', 'Jl. Hotel India']}
destination = ['H']

testvar = None

print(dict1[destination[-1]][0])
print("===")
if dict1[destination[-1]] is not None:
    print(destination)
    print("destination[-1] is " + destination[-1])
    print("dict1[destination[-1]] is " + str(dict1[destination[-1]]))
    print("---")
    destination.append(dict1[destination[-1]])

    print(dict1)
    print(destination)
    testvar = dict1[destination[-1][0]]
    print(dict1[destination[-1][0]])
    print("---")

destination.reverse()

print("===")
print(destination)
print("===")

print("Dari ", end="")
print(" pergi ke ".join(destination))
