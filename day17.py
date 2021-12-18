from re import findall
input = open('input/day17.txt', 'r').read()
x0, x1, y0, y1 = list(map(int, findall('(-?\d+)', input)))
    
def xs(v, x = 0):
    while x <= x1:
        yield x
        x += v
        v -= (v > 0)

def ys(v, y = 0):
    while y >= y0:
        yield y
        y += v
        v -= 1

def part1():
    for vy in range(-y0+1, 0, -1):
        if any([y0<=y<=y1 for y in ys(vy)]):
            return int(vy*(vy+1)/2)

def part2():
    return sum([any([x0<=p[0]<=x1 and y0<=p[1]<=y1 for p in zip(xs(x), ys(y))]) for x in range(1, x1+1) for y in range(y0, -y0+1)])

print(f'Solution to part 1: {part1()}')
print(f'Solution to part 2: {part2()}')