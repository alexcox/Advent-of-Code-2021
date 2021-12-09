input = []
with open('input/day8.txt', 'r') as f:
    for line in f.read().splitlines():
        line = list(map(lambda x: list(map(lambda y: "".join(sorted(y)), x.strip().split(' '))), line.split('|')))
        input.append(line)
f.close()

known = {2: 1, 4: 4, 3: 7, 7: 8}

def part1():
    return sum([sum([1 if len(y) in known else 0 for y in x[1]]) for x in input])

def part2():
    solution = 0
    for x in input:
        d = {}
        l = {len(k):k for k in x[0]}
        tmp = 0
        for y in range(len(x[0])):
            n = len(x[0][y])
            k = x[0][y]
            if n == 5: # 2, 3, 5
                if set(l[3]).issubset(set(x[0][y])): # 3
                    d[k] = 3
                elif len([k for k in list(x[0][y]) if k in list(l[4])]) == 3: # 5
                    d[k] = 5
                else: # 2
                    d[k] = 2
            elif n == 6: # 0, 6, 9
                if set(l[4]).issubset(set(x[0][y])): # 9
                    d[k] = 9
                elif set(l[3]).issubset(set(x[0][y])): # 0
                    d[k] = 0
                else: # 6
                    d[k] = 6
            else: # 1, 4, 7, 8
                d[k] = known[n]
        for y in range(4):
            j = 10**(4 - y - 1) * d[x[1][y]]
            tmp += 10**(4 - y - 1) * d[x[1][y]]
        solution += tmp
    return solution

print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")