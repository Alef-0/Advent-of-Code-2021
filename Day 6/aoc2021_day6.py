from os.path import join
from time import time_ns as time
import numpy as np

TEST = 'test_input6.txt'
INPUT = 'input6.txt'
LOCAL = "Day 6"
school = []
start = time()

with open(join(LOCAL,INPUT)) as file: 
    original = list(map(int,file.read().split(',')))

part1 = 80
part2 = 256

def create(days, school, conception, timer, times = 1):
    new_fish = (timer + 1)  + conception
    rest = days - new_fish
    if rest >= 0: 
        school[new_fish] += 1 * times
    total = rest // 7
    for i in range(1, total + 1):
        new_conception = new_fish + 7 * i
        if new_conception > days: return
        school[new_fish + 7 * i] += 1 * times
    return

# Part 1
# Test = 5934 | INPUT = 388739
school = np.zeros(part1 + 1)
school[0] = len(original)
for day in range(part1 + 1):
    # First iteration
    if day == 0: 
        for fish in original: 
            create(part1, school, 0, fish)
    else: 
            create(part1, school,day, 8, school[day])
print('Part 1: ', sum(school))

# Part 2
# Test = 26984457539 | INPUT = 1741362314973
school = np.zeros(part2 + 1)
school[0] = len(original)
for day in range(part2 + 1):
    # First iteration
    if day == 0: 
        for fish in original: 
            create(part2, school, 0, fish)
    else: 
            create(part2, school,day, 8, school[day])
print('Part 2: ', sum(school))

print("Time elapsed in ns: ", time() - start)