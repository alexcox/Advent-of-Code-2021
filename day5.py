with open('input/day5.txt', 'r') as f:
    input = [[list(map(int, x[0].split(','))), list(map(int, x[-1].split(',')))] for x in [line.split() for line in f.read().splitlines()]]
f.close()

def hydrothermalVents(diagonals=False):
    grid = {}
    for line in input:
        (x0, y0, x1, y1) = line[0] + line[1]
        if (x0 == x1):
            for i in range(min(y0, y1), max(y0, y1) + 1):
                grid[(x0, i)] = grid[(x0, i)] + 1 if (x0, i) in grid else 1
        elif (y0 == y1): 
            for i in range(min(x0, x1), max(x0, x1) + 1):
                grid[(i, y0)] = grid[(i, y0)] + 1 if (i, y0) in grid else 1
        elif diagonals:
            for i in range(x0, x1 + 1 * int((x1 - x0)/abs(x1 - x0)), int((x1 - x0)/abs(x1 - x0))):
                y_dir = int((y1 - y0)/abs(y1 - y0))
                grid[(i, y0 + abs(x0 - i)*y_dir)] = grid[(i, y0 + abs(x0 - i)*y_dir)] + 1 if (i, y0 + abs(x0 - i)*y_dir) in grid else 1
    return sum([1 for v in grid.values() if v > 1])

print("Solution to part 1: " + str(hydrothermalVents()))
print("Solution to part 2: " + str(hydrothermalVents(True)))

