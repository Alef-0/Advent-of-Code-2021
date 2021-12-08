# This one is not trying to be optimal
# It will run and not finish if the days are drifiting close to part 2 ~ 170
# It's just interesting to see a obvious approach for a inneficient problem
# And many did the same just to pass from part 1
from os.path import join
from time import time_ns as time

TEST = 'test_input6.txt'
INPUT = 'input6.txt'
LOCAL = "Day 6"
school = []
start = time()

with open(join(LOCAL,TEST)) as file: 
    school = list(map(int,file.read().split(',')))

copy_school = school.copy()

part1 = 80
part2 = 260

for j in range(part1):
    add = 0
    for i in range(len(school)):
        if school[i] == 0: add += 1; school[i] = 6
        else: school[i] -= 1
    if add != 0: school += [8] * add

print('Part 1: ', len(school))

school = copy_school.copy()

for j in range(part2):
    add = 0
    for i in range(len(school)):
        if school[i] == 0: add += 1; school[i] = 6
        else: school[i] -= 1
    if add != 0: school += [8] * add
    print("In day: ", j)


print('Part 2: ', len(school))