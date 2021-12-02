with open('input/day1.txt', 'r') as f:
    input = list(map(int, f.read().splitlines()))
f.close()

def part1():
    last = input[0]
    count = 0
    for i in input[1:]:
        if i > last:
            count += 1
        last = i
    return count

def part2():
    last = input[0] + input[1] + input[2]
    count = 0
    for i in range(3, len(input)):
        s = input[i] + input[i - 1] + input[i - 2]
        if s > last:
            count += 1
        last = s
    return count

print("Solution to part 1: " + str(part1()))
print("Solution to part 2: " + str(part2()))