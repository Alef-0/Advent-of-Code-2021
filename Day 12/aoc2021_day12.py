from collections import defaultdict
from time import time_ns as time
from os.path import join

INPUT = 'input12.txt'
TEST = 'test12.txt'
LOCAL = 'Day 12'
start = time()

caves = defaultdict(list)

with open(join(LOCAL, INPUT)) as file:
    data = file.read().split()

for paths in data:
    left, right = paths.split('-')
    caves[left].append(right)
    caves[right].append(left)

total = 0
def path(caves, current, stack, part2=False):
    global total
    if not part2:
        if current.isupper() or current not in stack: 
            stack.append(current)
        else: 
            return 
    else:
        lowers = [x for x in stack if x.islower()]
        if current.isupper() or len(set(lowers)) == len(lowers) or current not in stack:
            stack.append(current)
        else:
            return
    # See if it's the end
    if current == 'end': 
        stack.pop()
        global total
        total += 1
        return
    # Walk through all
    for next in caves[current]:
        if next == 'start': continue
        path(caves, next, stack, part2)
    stack.pop()
    return 

# Part 1
# TEST = 10 | INPUT = 4104
total = 0
stack = []
path(caves, 'start', stack)
print("Part 1:", total)
# Part 2
# TEST = 36 | INPUT = 119760
total = 0
stack = []
path(caves, 'start', stack, True)
print("Part 2:", total)

print("Time elapsed in ns", time() - start)