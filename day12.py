input = open('input/day12.txt', 'r').read().splitlines()
connections = {}
for connection in input:
    connection = connection.split('-')
    if connection[0] in connections:
        connections[connection[0]].append(connection[1])
    else:
        connections[connection[0]] = [connection[1]]
    if connection[1] in connections:
        connections[connection[1]].append(connection[0])
    else:
        connections[connection[1]] = [connection[0]]

def traverse_caves(small_caves = False, node = 'start', visited = ['start']):
    x = 0
    if node == 'end':
        return 1
    for neighbour in connections[node]:
        if neighbour.isupper():
            x += traverse_caves(small_caves, neighbour, visited)
        elif neighbour not in visited:
            x += traverse_caves(small_caves, neighbour, visited + [neighbour])
        elif small_caves and neighbour != 'start':
            x += traverse_caves(False, neighbour, visited)
    return x

print(f"Solution to part 1: {traverse_caves()}")
print(f"Solution to part 2: {traverse_caves(small_caves = True)}")