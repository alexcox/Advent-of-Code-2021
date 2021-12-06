fish = {}
with open('input/day6.txt', 'r') as f:
    for i in map(int, f.read().split(',')):
        fish[i] = fish.get(i, 0) + 1
f.close()

def count_fish(fish, days):
    for day in range(days):
        fish_temp = {}
        for k in fish:
            if k == 0:
                fish_temp[8] = fish_temp.get(8, 0) + fish[0]
                fish_temp[6] = fish_temp.get(6, 0) + fish[0]
            else:
                fish_temp[k - 1] = fish_temp.get(k - 1, 0) + fish[k]
        fish = fish_temp
    return sum(fish.values())

print("Solution to part 1: " + str(count_fish(fish, 80)))
print("Solution to part 2: " + str(count_fish(fish, 256)))
