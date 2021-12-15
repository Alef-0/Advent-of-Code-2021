from os.path import join, isfile
from time import time_ns as time

TEST = "input_test3.txt"
INPUT = "input3.txt"
LOCAL = 'Day 3'
start = time()
CHOICE = INPUT
if not isfile(CHOICE): CHOICE = join(LOCAL, CHOICE)

with open(CHOICE) as file: 
    binaries = list([line.strip() for line in file.readlines()])

# Part 1
# TEST = 198 | INPUT = 3985686
total = len(binaries)
size = len(binaries[0])
most, least = "", ""
for bit in range(size):
    ones = 0
    for numbers in binaries:
        if numbers[bit] == '1': ones += 1
    if ones >= total/2:  most += '1'; least += '0'
    else:               most += '0'; least += '1'
gamma = int(most,2); epsilon = int(least,2)
print("Part 1: ", gamma * epsilon)

# Part 2
# TEST = 230 | INPUT = 2555739
gamma, epsilon = "",""
original_copy = binaries.copy()
for bit in range(size):
    ones = 0
    for numbers in binaries:
        if numbers[bit] == '1': ones += 1
    if ones >= len(binaries)/2: binaries = [numbers for numbers in binaries if numbers[bit] == '1']
    else:                       binaries = [numbers for numbers in binaries if numbers[bit] == '0']
    if len(binaries) == 1: break
gamma = binaries[0]

binaries = original_copy
for bit in range(size):
    ones = 0
    for numbers in binaries:
        if numbers[bit] == '1': ones += 1
    if ones >= len(binaries)/2: binaries = [numbers for numbers in binaries if numbers[bit] == '0']
    else:                       binaries = [numbers for numbers in binaries if numbers[bit] == '1']
    if len(binaries) == 1: break
epsilon = binaries[0]

print("Part 2: ", int(gamma,2) * int(epsilon, 2))

print("Time elapsed in ns: ", time() - start)