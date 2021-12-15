polymer, input = open('input/day14.txt', 'r').read().split('\n\n')
insertion_rules, keys = dict(k.split(' -> ') for k in input.split('\n')), list('BCHNOVPKSF')

def polymer_difference(steps = 10):
    count = {k: polymer.count(k) for k in keys}
    pairs = {i + j: polymer.count(i + j) for i in keys for j in keys}
    for step in range(steps):
        d = {}
        for pair in pairs:
            el, n, pairs[pair] = insertion_rules[pair], pairs[pair], 0
            count[el] += n
            d[pair[0] + el], d[el + pair[1]] = d.get(pair[0] + el, 0) + n, d.get(el + pair[1], 0) + n
        pairs |= d
    return max(count.values()) - min(count.values())

print(f'Solution to part 1: {polymer_difference()}')
print(f'Solution to part 2: {polymer_difference(steps=40)}')