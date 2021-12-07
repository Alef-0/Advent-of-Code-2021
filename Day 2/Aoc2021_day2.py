TEST = "input_test2.txt"
INPUT = "input2.txt"

with open(INPUT) as file: instructions = [line.split() for line in file.readlines()]

# Part 1
# TEST = 150 | INPUT = 1636725
horizontal, depth = 0,0
for command, value in instructions:
    match command:
        case 'forward': horizontal  += int(value)
        case 'up':      depth       -= int(value)
        case 'down':    depth       += int(value)
        case _: pass
print('Part 1: ', horizontal * depth)

# Part 2
# TEST = 900 | INPUT = 1872757425
horizontal, aim, depth = 0,0,0
for command, value in instructions:
    match command:
        case 'forward': 
                        horizontal += int(value)
                        depth      += int(value) * aim
        case 'up':      aim        -= int(value)
        case 'down':    aim        += int(value)
        case _: pass
print('Part 2: ', horizontal * depth)


