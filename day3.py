with open('input/day3.txt', 'r') as f:
    input = list(map(lambda x: int(x, 2), f.read().splitlines()))
f.close()

def gammaRate():
    return "".join([str(round(sum([(j & 2**(11 - i)) >> (11 - i) for j in input])/len(input))) for i in range(12)])

def epsilonRate():
    return "".join(["1" if j == "0" else "0" for j in gammaRate()])

f = lambda x: 1 if x == 0.5 else round(x)

def oxygenGeneratorRating():
    copy = input
    while len(copy) > 1:
        for i in range(12):
            mcv = f(sum([(j & 2**(11 - i)) >> (11 - i) for j in copy])/len(copy))
            copy = list(filter(lambda x: (x & 2**(11 - i)) >> (11 - i) == mcv, copy))
            if (len(copy) == 1):
                return copy[0]

def co2ScrubberRating():
    copy = input
    while len(copy) > 1:
        for i in range(12):
            lcv = 1 - f(sum([(j & 2**(11 - i)) >> (11 - i) for j in copy])/len(copy))
            copy = list(filter(lambda x: (x & 2**(11 - i)) >> (11 - i) == lcv, copy))
            if (len(copy) == 1):
                return copy[0]

def part1():
    return int(gammaRate(), 2) * int(epsilonRate(), 2)

def part2():
    return oxygenGeneratorRating() * co2ScrubberRating()

print("Power consumption: " + str(part1()))
print("Life support rating: " + str(part2()))