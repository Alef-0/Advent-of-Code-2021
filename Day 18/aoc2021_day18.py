from math import ceil, floor
from os.path import join, isfile
from time import time_ns as time

TEST = 'test18.txt'
INPUT = 'input18.txt'
CHOICE = TEST
LOCAL = 'Day 18'
start = time()

if not isfile(CHOICE): CHOICE = join(LOCAL, CHOICE)
numbers = []
with open(CHOICE) as file:
    data = file.read().split('\n')
    map_function = lambda x: int(x) if x.isdigit() else x
    for number in data:
        add = list(filter(lambda x: x != ',', map(map_function, number)))
        numbers.append(add)
numbers_copy = numbers.copy()

def print_number(number):
    for i in range(len(number)):
        print(number[i], end='')
        if i + 1 == len(number): break
        if (isinstance(number[i], int) and isinstance(number[i+1], int) or
           (number[i] == ']' and number[i+1] == '[') and i+1 < len(number) or
           (isinstance(number[i], int) and number[i+1] == '[') or (isinstance(number[i+1], int) and number[i] == ']')):
            print(',', end = '')
    print()

def explosion(number, stop):
    left = number[stop]
    right = number[stop + 1]
    # Check the nearest number on the left
    iter = stop - 1 
    while iter > -1:
        if isinstance(number[iter], int): 
            number[iter] += left
            break
        iter -= 1
    # Check the nearest number on the right
    iter = stop + 2 # It's plus two to avoid finding the second number
    while iter < len(number):
        if isinstance(number[iter], int): 
            number[iter] += right
            break
        iter += 1
    # Delete the slice
    del number[stop - 1 : stop + 3]
    number.insert(stop -1, 0)

def split(number, stop):
    value = number[stop]
    left, right = floor(value/2), ceil(value/2)
    del number[stop]
    # Just insert in this order to avoid confusion
    number.insert(stop, ']')
    number.insert(stop, right)
    number.insert(stop, left)
    number.insert(stop, '[')
    pass

def solve(number):
    change = True
    while change:
        change = False
        # Check if explodes
        counter = 0
        stop = -1
        for i in range(len(number)):
            if number[i] == '[': counter += 1
            elif number[i] == ']': counter -= 1
            # (counter > 4) is enough because it counts the first '['
            if counter > 4 and isinstance(number[i], int) and number[i+2] == ']': 
                stop = i
                break
        if stop != -1: 
            explosion(number, stop)
            change = True
            continue
        # Check if splits
        stop = -1
        for i in range(len(number)):
            if isinstance(number[i], int) and number[i] > 9: 
                stop = i
                break
        if stop != -1:
            split(number, stop)
            change = True
            continue
    # Acabou e faz nada

def sum_numbers(number1, number2):
    new_numbers = []
    # First iteration
    new_numbers.append('[')
    new_numbers += number1
    new_numbers += number2
    new_numbers.append(']')
    return new_numbers

def magnitude(number):
    change = True
    while change:
        change = False
        for i in range(len(number)-1):
            if isinstance(number[i], int) and isinstance(number[i+1], int): 
                change = True
                new_value = 3*number[i] + 2*number[i+1]
                del number[i-1 : i+3]
                number.insert(i-1, new_value)
                break

    return number[0]


# PART 1
# TEST = 4140 | INPUT = 3725
solve(numbers[0])
while len(numbers) > 1: 
    solve(numbers[1])
    new_number = sum_numbers(numbers[0], numbers[1])
    del numbers[0:2]
    numbers.insert(0, new_number)
    solve(numbers[0])
# Result
print_number(numbers[0])
answer = magnitude(numbers[0])
print("Part 1: ", answer)

# PART 2
# TEST = 3993 | INPUT = 4832
biggest = 0
for i in range(len(numbers_copy)):
    for j in range(len(numbers_copy)):
        if i == j: continue
        new_number = sum_numbers(numbers_copy[i], numbers_copy[j])
        solve(new_number)
        new_value =  magnitude(new_number)
        if new_value > biggest: biggest = new_value
print("Part 2: ", biggest)

print("Time elapsed in ns: ", time() - start)