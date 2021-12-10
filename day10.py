input = open('input/day10.txt', 'r').read().splitlines()

delims = {'{': '}', '[': ']', '(': ')', '<': '>'}
delims_r = {y:x for x,y in delims.items()}

def part1():
    illegal_chars = []
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for line in input:
        line = list(line)
        queue = []
        while line:
            s = line.pop(0)
            if s in delims:
                queue.append(s)
            else:
                e = queue.pop()
                if e != delims_r[s]: # corrupt
                    illegal_chars.append(s)
                    break
    return sum([scores[i] for i in illegal_chars])

def part2():
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    incomplete_scores = []
    for line in input:
        line = list(line)
        queue = []
        while line:
            s = line.pop(0)
            if s in delims:
                queue.append(s)
            else:
                e = queue.pop()
                if e != delims_r[s]: # corrupt
                    break
            if not line and queue: # incomplete
                tmp = 0
                for q in queue[::-1]:
                    tmp *= 5
                    tmp += scores[q]
                incomplete_scores.append(tmp)
    return sorted(incomplete_scores)[int(len(incomplete_scores)/2)]

print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")