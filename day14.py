input = [x.split('\n') for x in open('input/day14.txt', 'r').read().split('\n\n')]
polymer, insertion_rules = input[0][0], {k.split(' -> ')[0]:k.split(' -> ')[1] for k in input[1]}

def polymer_difference(steps = 10):
    keys = list('BCHNOVPKSF')
    count = {k:polymer.count(k) for k in keys}
    pairs = {i + j: polymer.count(i + j) for i in keys for j in keys}
    for step in range(steps):
        d = {}
        for pair in pairs:
            if pairs[pair] > 0:
                el, n, pairs[pair] = insertion_rules[pair], pairs[pair], 0
                count[el] += n
                d[pair[0] + el], d[el + pair[1]] = d.get(pair[0] + el, 0) + n, d.get(el + pair[1], 0) + n
        for k in d: pairs[k] += d[k]
    return max(count.values()) - min(count.values())

print(f'Solution to part 1: {polymer_difference()}')
print(f'Solution to part 2: {polymer_difference(steps=40)}')