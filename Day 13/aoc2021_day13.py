import numpy as np
TEST = 'test13.txt'
INPUT = 'input13.txt'
MAX_SIZE = 15

folds = []
marks_x, marks_y = [], []
with open(INPUT) as file: 
    while line := file.readline():
        if line == '\n': pass
        elif len(values := line.split(',')) == 2:
            column,line = list(map(int,values))
            marks_x.append(column); marks_y.append(line)
        else:
            _, _, fold = values[0].split()
            folds.append(fold)

# Create the matrix
matrix = []
for lines in range(max(marks_y)+1):
    matrix.append([])
    matrix[lines] = ['.'] * (max(marks_x) + 1)
matrix = np.array(matrix, dtype=str)

# Mark the matrix
for column,line in zip(marks_x, marks_y):
    matrix[line, column] = '#'
# print(matrix)
# print(folds)

def fold(matrix, place):
    coordinate, number = place.split('=')
    if coordinate == 'x': 
        column_fold = int(number); line_fold = 0
        first_half, second_half = matrix[:, :column_fold], matrix[:, column_fold + 1:]
    else: 
        # print('ENTROU Y')
        line_fold = int(number); column_fold = 0
        first_half, second_half = matrix[:line_fold, :], matrix[line_fold + 1:, :]

    # print(first_half)
    # print()
    # print(second_half)

    # Pass the matrix
    for line in range(max_line := min(len(second_half), len(first_half))):
        for column in range(max_column := min(len(second_half[line]), len(first_half[line]))):
            if second_half[line, column] == '#': 
                if line_fold == 0: 
                    # print(line, max_column - column - 1)
                    first_half[line, max_column - column - 1]  = '#'
                else:         
                    # print(max_line - line - 1, column, 'line', line)
                    first_half[max_line - line - 1, column]    = '#'
    
    # print()
    # print(first_half)

    return first_half.copy()



# Part 1 | INPUT: 607
matrix = fold(matrix, folds[0])
print('Part 1: ', np.sum(matrix == '#') )
for i in range(1, len(folds)): matrix = fold(matrix, folds[i])
for lines in matrix:
    for chars in lines:
        if chars == '.': print(' ', end='')
        else: print(chars, end='')
    print()
# PART 2 | CPZLPFZL