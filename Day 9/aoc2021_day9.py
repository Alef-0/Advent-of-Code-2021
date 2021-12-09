from os.path import join
from collections import Counter
from time import time_ns as time
from numpy import array

TEST = 'test9.txt'
INPUT = 'input9.txt'
LOCAL = 'Day 9'
start = time()

with open(join(LOCAL, INPUT)) as file: 
    points = file.read().split()
    for i in range(len(points)):
        points[i] = list(map(int,list(points[i])))
        points[i].append(9)
    max_length = len(points[0]) - 1 - 1 # The extra 1 is for out of bounds
    max_depth = len(points) - 1
    points.append([9] * (max_length + 2))
    sea_floor = array(points)

# PART 1
# TEST = 15 | INPUT = 475
def find_low_points(sea_floor : array):
    amount = 0
    low_points = []
    # Iterate trough all
    for lines in range(max_depth + 1):
        for columns in range(max_length + 1):
            if (
                ((lines == 0) or          (sea_floor[lines - 1, columns] > sea_floor[lines,columns])) and # UP
                ((lines == max_depth) or  (sea_floor[lines + 1, columns] > sea_floor[lines,columns])) and # DOWN
                ((columns == 0) or        (sea_floor[lines, columns - 1] > sea_floor[lines,columns])) and # LEFT
                ((columns == max_length)or(sea_floor[lines, columns + 1] > sea_floor[lines,columns]))     # RIGHT
            ):
                amount += 1
                low_points.append(sea_floor[lines, columns])
    return amount, low_points

# print(sea_floor)
amount, low_points = find_low_points(sea_floor)
total = 0
for i in low_points: total += i + 1
print('Part 1: ', total)

# PART 2
# TEST = 1134 | INPUT = 1092012
def fill(sea_floor : array, line, column, size_tracker, position):
    if sea_floor[line, column] == 9: return
    else: sea_floor[line, column] = 9
    # Recursive
    size_tracker[position] += 1
    if line != 0:           fill(sea_floor, line - 1, column, size_tracker, position)    # UP
    if line != max_depth:   fill(sea_floor, line + 1, column, size_tracker, position)    # DOWN
    if column != 0:         fill(sea_floor, line, column - 1, size_tracker, position)    # LEFT
    if column != max_length:fill(sea_floor, line, column + 1, size_tracker, position)    # RIGHT
    return


def find_basins(sea_floor : array):
    amount = -1
    sizes = []
    for lines in range(max_depth + 1):
        for columns in range(max_length + 1):
            if sea_floor[lines, columns] != 9:
                amount += 1
                sizes.append(0)
                # print("Before \n", sea_floor)
                fill(sea_floor, lines, columns, sizes, amount)
                # print("After \n ", sea_floor)
    # Return in order
    sizes.sort(reverse = True)
    return amount,sizes

amount, sizes = find_basins(sea_floor)
print('PART 2: ', sizes[0] * sizes[1] * sizes[2])

print("Time elapsed in ns: ", time() - start)