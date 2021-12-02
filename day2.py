with open('input/day2.txt', 'r') as f:
    input = [(k.split()[0], int(k.split()[1])) for k in f.read().splitlines()]
f.close()

def part1():
    x = 0
    y = 0
    for (direction, magnitude) in input:
        if direction == 'forward':
            x += magnitude
        elif direction == 'up':
            y -= magnitude
        elif direction == 'down':
            y += magnitude
    return x*y

def part2():
    x = 0
    y = 0
    aim = 0
    for (direction, magnitude) in input:
        if direction == 'forward':
            x += magnitude
            y += magnitude * aim
        elif direction == 'up':
            aim -= magnitude
        elif direction == 'down':
            aim += magnitude
    return x*y
    
print("Solution to part 1: " + str(part1()))
print("Solution to part 2: " + str(part2()))
