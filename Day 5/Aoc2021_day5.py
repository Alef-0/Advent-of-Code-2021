from os.path import join
from time import time_ns as time
import numpy as np

TEST = 'input_test5.txt'
INPUT = 'input5.txt'
LOCAL = "Day 5"
DIMENSIONS = 1000 # It's normally ~ 1000
# This one is not efficient
start_time = time()

start, end = [],[]
copy_start = start.copy()
copy_end = end.copy()
with open(join(LOCAL,INPUT)) as file:
    instructions = file.readlines()
    for line in instructions:
        left, right = line.split(' -> ')
        start.append([int(x) for x in left.split(',')])
        end.append([int(x) for x in right.split(',')])

def fill(grid, p1, p2, part2 = False):
    # defining ranges
    # If it's growing or decreasing
    step1 = 1 if p2[0] >= p1[0] else -1
    step2 = 1 if p2[1] >= p1[1] else -1

    if not part2:
        for i in range(p1[0], p2[0] + step1, step1):
            for j in range(p1[1], p2[1] + step2, step2):
                if p1[0] == p2[0] or p1[1] == p2[1]: 
                    grid[i][j] += 1 
    else:
        # This one makes use of diagonal counters, if they are equal it's a 45 degree angle
        di1 = -1; di2 = -1
        for i in range(p1[0], p2[0] + step1, step1):
            di1 += 1
            for j in range(p1[1], p2[1] + step2, step2):
                if p1[0] == p2[0] or p1[1] == p2[1]: 
                    grid[i][j] += 1 
                else: 
                    di2 += 1
                    if di2 == di1:
                        grid[i][j] += 1 
                        break
            di2 = -1
    return

# Part 1
# TEST = 5 | INPUT = 5280
grid = np.zeros((DIMENSIONS,DIMENSIONS), dtype = np.uint8)

for p1,p2 in zip(start,end): fill(grid, p1, p2)
total = 0
for line in grid: 
    for numbers in line:
        if numbers >= 2: 
            total += 1
print("Part 1: ", total)

# Part 2
# TEST = 12 | INPUT = 16716
grid = np.zeros((DIMENSIONS,DIMENSIONS))

for p1,p2 in zip(start,end): fill(grid,p1,p2, True)
total = 0
for line in grid: 
    for numbers in line:
        if numbers >= 2: 
            total += 1
print("Part 2: ", total)

print("Time elapsed in ns: ", time() - start_time)
# If you want to see the grid after all it needs to be transposed
# Since the first indice are lines and then columns
# print(grid.transpose())