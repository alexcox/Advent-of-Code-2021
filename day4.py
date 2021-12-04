import numpy as np

with open('input/day4.txt', 'r') as f:
    input = [line.strip() for line in f.read().splitlines() if line.strip()]
f.close()

numbers = list(map(int, input[0].split(',')))
input = list(map(lambda x: list(map(int, x.replace('  ', ' ').split(' '))), input[1:]))
n_boards = int(len(input)/5)
boards = []
for i in range(n_boards):
    boards.append(np.matrix(input[i*5: (i+1)*5]))
sol = [-1, -1, -1, -1, -1]

def part1():
    sol_found = False
    b = boards
    sol_index = 0
    sol_number = 0
    for i in numbers:
        for j in range(len(b)):
            b[j][b[j] == i] = -1
            if sol in b[j].tolist() or sol in b[j].transpose().tolist():
                sol_number = i
                sol_found = True
                sol_index = j
                sol_board = b[j]
        if sol_found == True:
            break
    sol_board[sol_board == -1] = 0
    solution = sol_board.sum() * sol_number
    return (sol_index, solution)

def part2():
    solution = 0
    while len(boards) > 0:
        (i, solution) = part1()
        boards.pop(i)
    return solution

print("Solution to part 1: " + str(part1()[1]))
print("Solution to part 2: " + str(part2()))