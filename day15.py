import heapq

input = [list(map(int, list(x))) for x in open('input/day15.txt', 'r').read().splitlines()]
n = len(input)

def neighbours(x, y, _=n):
    t = [-1, 0, 1]
    return [(x+i, y+j) for i in t for j in t if abs(i) != abs(j) and 0 <= x + i < _ and 0 <= y + j < _]

def scale_grid(size = 2):
    return [[(i//n + j//n + input[i % n][j % n]) % 10 + (i//n + j//n + input[i % n][j % n])//10 \
         for j in range(n*size)] for i in range(n*size)]

def path(grid = input):
    n_grid = len(grid)
    target, q = (n_grid - 1, n_grid - 1), [(0, (0, 0))]
    dist = {(i, j): float("inf") for i in range(n_grid) for j in range(n_grid)}
    dist[0, 0] = 0
    heapq.heapify(q)
    while q:
        d, u = heapq.heappop(q)
        if u == target: return d
        for v in neighbours(*u, n_grid):
            alt = d + grid[v[0]][v[1]]
            if alt < dist[v]:
                heapq.heappush(q, (alt, v))
                dist[v] = alt

print(f'Solution to part 1: {path()}')
print(f'Solution to part 2: {path(grid=scale_grid(5))}')