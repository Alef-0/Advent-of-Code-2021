from statistics import median
from os.path import join

stack = []

PARENTHESES = 3
BRACKETS = 57
BRACES = 1197
CHEVRONS = 25137
LOCAL = "Day 10"

TEST = 'test10.txt'
INPUT = 'input10.txt'

with open(join(LOCAL,TEST)) as file: data = file.read().split()

def calculate(part2 = False):
    total = 0
    results = []
    for line in data:
        total_2 = 0
        add = 0
        for char in line:
            if char in '{[(<': stack.append(char)
            else:
                closing = stack.pop()
                if   closing != '(' and char == ')': add += PARENTHESES
                elif closing != '[' and char == ']': add += BRACKETS
                elif closing != '{' and char == '}': add += BRACES
                elif closing != '<' and char == '>': add += CHEVRONS

                if add:
                    total += add; 
                    break
        
        complete = False
        while len(stack) > 0 and part2 and not add: 
            complete = True
            missing  = stack.pop()
            total_2 *= 5
            match missing:
                case '(': total_2 += 1
                case '[': total_2 += 2
                case '{': total_2 += 3
                case '<': total_2 += 4
        stack.clear()
        if part2 and complete: results.append(total_2)
    
    if part2: return median(results)
    return total

# PART 1
# TEST = 26397 | INPUT = 339477
total = calculate()
print('Part 1: ', total)
# PART 2
# TEST = 288957 | INPUT = 3049320156
total = calculate(True)
print('Part 2: ', total)
            