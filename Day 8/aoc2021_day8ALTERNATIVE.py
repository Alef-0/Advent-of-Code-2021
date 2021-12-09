# This one sees the pattern that one segment si X time on in all numbers

from os.path import join
from time import time_ns as time


TEST = 'test_input8.txt'
INPUT = 'input8.txt'
LOCAL = 'Day 8'
start = time()

sequences, outputs = [],[]
with open(join(LOCAL, INPUT)) as file:
    entrys = file.readlines()
    for line in entrys:
        left, right = line.split(' | ')
        sequences.append(left.split())
        outputs.append(right.split())

# Part 1
# TEST = 26 | OUTPUT = 495
def easy_numbers(outputs):
    amount = 0
    for digit in outputs:
        if len(digit) in [2, 3, 4, 7]:
            amount += 1
    return amount

total = 0
for i in outputs:
    total += easy_numbers(i)
print("Part 1: ", total)

# Part 2
# TEST = 61229 | INPUT = 1055164
def sort_string(string): return ''.join(sorted(list(string)))

def get_number(dictionary : dict, outputs):
    result = 0
    for i in outputs:
        sorted_string = sort_string(i)
        # print(sorted_string)
        for i in range(10):
            if sorted_string == dictionary[i]: 
                result = 10 * result + i
    return result

def solver(sequences):
    numbers : list[str] = [''] * 10
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    appearance = {'a': 0, 'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0}
    wires = {'a': '', 'b': '','c': '','d': '','e': '','f': '','g': ''}
    # Find first the easiest
    numbers[1], = [i for i in sequences if len(i) == 2]
    numbers[4], = [i for i in sequences if len(i) == 4]
    numbers[7], = [i for i in sequences if len(i) == 3]
    numbers[8], = [i for i in sequences if len(i) == 7]

    # (e) appears four times
    for j in sequences:
        for i in j: 
            appearance[i] += 1
    
    for key, values in appearance.items():
        if   (values == 8) and (key not in numbers[1]): wires['a'] = key
        elif (values == 6):                             wires['b'] = key
        elif (values == 8) and (key in     numbers[1]): wires['c'] = key
        elif (values == 7) and (key in     numbers[4]): wires['d'] = key
        elif (values == 4):                             wires['e'] = key
        elif (values == 9):                             wires['f'] = key
        elif (values == 7) and (key not in numbers[4]): wires['g'] = key

    # Create a new sequence with the numbers
    numbers[0] = sort_string(numbers[8].replace(wires['d'],''))
    numbers[1] = sort_string(numbers[1])
    numbers[2] = sort_string(wires['a'] + wires['c'] + wires['d'] + wires['e'] + wires['g'])
    numbers[3] = sort_string(numbers[7] + wires['d'] + wires['g'])
    numbers[4] = sort_string(numbers[4])
    numbers[5] = sort_string(wires['a'] + wires['b'] + wires['d'] + wires['f'] + wires['g'])
    numbers[6] = sort_string(numbers[8].replace(wires['c'],''))
    numbers[7] = sort_string(numbers[7])
    numbers[8] = sort_string(numbers[8])
    numbers[9] = sort_string(numbers[8].replace(wires['e'],''))

    # print(wires)
    return numbers

total = 0
for left, right in zip(sequences, outputs):
    dictionary = solver(left)
    # print(dictionary)
    total+= get_number(dictionary, right)
print('Part 2: ', total)

print('Time elapsed in ns: ', (time() - start)/100000)