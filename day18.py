input = [eval(x) for x in open('input/day18.txt', 'r').read().splitlines()]

def explode(s):
    i, depth = 0, 0
    while True:
        if i == len(s): break
        depth += (s[i] == '[') - (s[i] == ']')
        if depth >= 5 and s[i] == '[' and s[i+1].isnumeric() and s[i+4].isnumeric():
            l, r = int(s[i+1]), int(s[i+4])
            for k in range(i-1, -1, -1):
                if s[k].isnumeric(): s[k] = str(int(s[k]) + l); break
            for k in range(i+6, len(s)):
                if s[k].isnumeric(): s[k] = str(int(s[k]) + r); break
            s[i:i+6] = ['0']
            i, depth = 0, 0
        else: i += 1
    return s

def split(s, i = 0):
    while True:
        if i == len(s): break
        if s[i].isnumeric() and int(s[i]) > 9:
            return s[:i] + ['[', str(int(s[i])//2), ',', ' ', str((int(s[i])+1)//2), ']'] + s[i+1:]
        i += 1
    return s

def magnitude(s):
    n_open, n_close, n_pair, total = 0, 0, 0, 0
    for i in s:
        n_pair += (i == ',')
        n_open += (i == '[')
        n_close += (i == ']')
        if i.isnumeric(): total += 3**(n_open - n_pair)*2**(n_pair - n_close)*int(i)
    return total

def part1():
    snailfish = input[0]
    for x in input[1:]:
        snailfish = [snailfish, x]
        sfs = list(str(snailfish))
        while True:
            e = explode(sfs)
            s = split(e)
            if sfs == s: break
            else: sfs = s
        snailfish = eval(''.join(sfs))
    return magnitude(sfs)

def part2():
    m = 0
    for i in range(100):
        for j in range(100):
            if i != j:
                sfs = list(str([input[i], input[j]]))
                while True:
                    e = explode(sfs)
                    s = split(e)
                    if sfs == s: break
                    else: sfs = s
                k = magnitude(sfs)
                m = k if k > m else m
    return m

print(f'Solution to part 1: {part1()}')
print(f'Solution to part 2: {part2()}')