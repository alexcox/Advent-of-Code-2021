input = [x.split('\n') for x in open('input/day13.txt', 'r').read().split('\n\n')]
points = {(int(k[0]), int(k[1])): 1 for k in [x.split(',') for x in input[0]]}

def fold(single_fold = True):
    p, max_x, max_y = points, 1309, 892
    for fold in input[1]:
        fold_axis, fold_value = fold.split('=')[0][-1], int(fold.split('=')[1])
        max_x, max_y = max_x if fold_axis == 'y' else int(max_x / 2), max_y if fold_axis == 'x' else int(max_y / 2)
        for (x, y) in list(p.keys()):
            if fold_axis == 'y' and y > fold_value:
                p[x, fold_value - (y - fold_value)] = 1
            elif fold_axis == 'x' and x > fold_value:
                p[fold_value - (x - fold_value), y] = 1
        if single_fold: return sum([1 if (i, j) in p else 0 for i in range(max_x) for j in range(max_y)])
    return '\n' + '\n'.join(["".join(['#' if (i,j) in p else '.' for i in range(max_x)]) for j in range(max_y)])

print(f'Solution to part 1: {fold()}')
print(f'Solution to part 2: {fold(single_fold = False)}')