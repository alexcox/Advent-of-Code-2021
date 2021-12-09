from math import prod

input = [[int(x) for x in list(line.strip())] for line in open('input/day9.txt').readlines()]

def adjacent(x, y, ignore = False):
    adj = []
    if x > 0 and (not ignore or (x-1, y) not in ignore):
        adj.append((x-1,y))
    if x < len(input) - 1 and (not ignore or (x+1, y) not in ignore):
        adj.append((x+1,y))
    if y > 0 and (not ignore or (x, y-1) not in ignore):
        adj.append((x,y-1))
    if y < len(input[x]) - 1 and (not ignore or (x, y+1) not in ignore):
        adj.append((x,y+1))
    return adj

def is_low_point(x, ignore = []):
    return all([input[x[0]][x[1]] < input[i[0]][i[1]] for i in adjacent(x[0], x[1]) if i not in ignore])

def part1():
    return sum([1 + input[x][y] for x in range(len(input)) for y in range(len(input[x])) if is_low_point((x, y))])

def part2():
    low_points, k = [(x,y) for x in range(len(input)) for y in range(len(input[x])) if is_low_point((x, y))], []
    for (x, y) in low_points:
        basin, q = [(x, y)], [(x, y)]
        while q:
            s = q.pop()
            for n in adjacent(s[0], s[1], basin):
                if input[n[0]][n[1]] > input[s[0]][s[1]] and input[n[0]][n[1]] != 9:
                    basin.append(n)
                    q.append(n)
        k.append(len(basin))
    return prod(sorted(k)[-3:])

print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")

