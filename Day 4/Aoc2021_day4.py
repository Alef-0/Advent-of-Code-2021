TEST = "input_test4.txt"
INPUT = "input4.txt"
BINGO_SIZE = 25
import numpy as np

bingos = []
with open(INPUT) as file: 
    numbers = [nums.strip() for nums in file.readline().split(',')]
    _ = file.readline() # Empty Line
    rest = file.read().split()
    bingos = []
    for i in range(0,len(rest) , BINGO_SIZE):
        board = rest[i : i + BINGO_SIZE]
        bingos.append(
            np.array([board[0:5],
                      board[5:10],
                      board[10:15],
                      board[15:20],
                      board[20:25]])
        )

check = [True] * len(bingos)

# It will be checked into a singular functions
def count(board, number):
    total = 0
    for i in range(5):
        for j in range(5):
            if board[i][j]: 
                total += int(board[i,j])
    return total * int(number)

points = []
def mark(number):
    # Check the number
    for board in bingos: 
        for line in range(5):
            for column in range(5):
                if board[line,column] == number: 
                    board[line,column] = ''
    # See if it's a victory
    for i in range(len(bingos)):
        if check[i]:
            for j in range(5):
                # Only lines and columns
                if not any(bingos[i][:,j]) or not any(bingos[i][j,:]) and check:
                    points.append(count(bingos[i], number))
                    check[i] = False

# Part 1
# TEST = 4512 | INPUT = 69579
points = []
for i in numbers: mark(i)
print('Part 1: ', points[0])
print("Part 2: ", points[-1])
# Part 2
# TEST = 1924 | INPUT = 14877