TEST = 'test_input7.txt'
INPUT = 'input7.txt'

with open(INPUT) as file: 
    crabs = list(map(int,file.read().split(',')))

from statistics import median

def calculate_fuel(position, part2 = True):
    fuel = 0
    for i in crabs:
        distance = abs(position - i)
        if part2: fuel += distance * (distance + 1) / 2
        else: fuel += distance
    return fuel
    
# Part 1
# TEST = 37 | INPUT = 343441
# The median is always the closest to all paths
best = median(crabs)
answer = calculate_fuel(best, False)
print("Part 1: ", answer)

# Part 2
# TEST = 168 | INPUT = 98925151
# In some test cases you can use the mean rounded 
# As the best case, but it's not garanteed

low, high = min(crabs), max(crabs)
# Edge cases
if   answer := calculate_fuel(low)  <= calculate_fuel(low + 1): pass
elif answer := calculate_fuel(high) <= calculate_fuel(high -1): pass
else:
    middle = (low + high) // 2
    before = -1 
    while low != high:
        if before == middle: break
        value = calculate_fuel(middle)
        right = calculate_fuel(middle + 1)
        left = calculate_fuel(middle - 1)
        
        if value < right and value >= left: high = middle
        elif value >= right and value < left: low = middle

        before = middle
        middle = (low + high) // 2
    answer = calculate_fuel(middle) 
    
print("Part 2: ", answer)

