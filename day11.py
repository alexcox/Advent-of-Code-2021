import copy
input = [[int(x) for x in list(line.strip())] for line in open('input/day11.txt').readlines()]

steps = 100
n = len(input)

def adjacent(x, y):
    t = [-1, 0, 1]
    return [(x+i, y+j) for i in t for j in t if not (i == 0 and j == 0) and 0 <= x + i < n and 0 <= y + j < n]

def part1():
    n_flash = 0
    grid = copy.deepcopy(input)
    for step in range(steps):
        flashed = []
        for x in range(n):
            for y in range(n):
                queue = [(x, y)]
                while queue:
                    k = queue.pop()
                    if grid[k[0]][k[1]] == 9: # flash
                        grid[k[0]][k[1]] = 0
                        queue += adjacent(k[0], k[1])
                        flashed.append(k)
                        n_flash += 1
                    elif k not in flashed:
                        grid[k[0]][k[1]] += 1
    return n_flash

def part2():
    step = 0
    while True:
        step += 1
        flashed = []
        for x in range(n):
            for y in range(n):
                queue = [(x, y)]
                while queue:
                    k = queue.pop()
                    if input[k[0]][k[1]] == 9: # flash
                        input[k[0]][k[1]] = 0
                        queue += adjacent(k[0], k[1])
                        flashed.append(k)
                    elif k not in flashed:
                        input[k[0]][k[1]] += 1
        if len(flashed) == n * n:
            return step
            
print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")