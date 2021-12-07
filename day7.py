import statistics

with open('input/day7.txt', 'r') as f:
    input = list(map(int, f.read().split(',')))
f.close()

def part1():
    return int(sum([abs(i - statistics.median(input)) for i in input]))

def part2():
    # .5 has to be rounded down
    x = int(statistics.mean(input)) if statistics.mean(input) - int(statistics.mean(input)) < 0.6 else round(statistics.mean(input))
    return int(sum([abs(i - x) * (abs(i - x) + 1)/2 for i in input]))

print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")