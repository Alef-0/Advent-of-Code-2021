import numpy as np
from time import time_ns as time
from os.path import join, isfile

TEST = 'test11.txt'
INPUT = 'input11.txt'
LOCAL = 'Day 11'
start = time()
CHOICE = INPUT
if not isfile(CHOICE): CHOICE = join(LOCAL, CHOICE)


with open(CHOICE) as file: matrix = file.read().split()

class Map():
    def __init__(self, matrix):
        map_list = []
        for line in range(len(matrix)):
            map_list.append([])
            for char in matrix[line]:
                map_list[line].append(int(char))
            map_list[line].append(int(10))
        map_list.append([10] * 11)
        self.matrix = np.array(map_list)
        
        # Now making tem blink
        flashing = []
        for i in range(10):
            flashing.append([False] * 10)
            flashing[i].append(True) 
        flashing.append([True] * 11)
        self.flashing = np.array(flashing, dtype = bool)
        
        # Counting everything
        self.total = 0
        self.day = 0
        self.all_flashed = False
        self.day_all_flashed = -1

    def update(self):
        # Add everything to one
        self.matrix += 1
        # See what flashed
        flashed = True
        while flashed:
            flashed = False
            for line in range(10):
                for column in range(10):
                    if  self.matrix[line][column] > 9 and not self.flashing[line,column]:
                        #Flashed 
                        flashed = True
                        self.total += 1
                        self.matrix[line][column] = 0
                        self.flashing[line,column] = True
                        # Add to each part of the surrounding if they did not flash yet
                        if not self.flashing[line-1][column]: self.matrix[line-1][column] += 1
                        if not self.flashing[line+1][column]: self.matrix[line+1][column] += 1
                        if not self.flashing[line][column-1]: self.matrix[line][column-1] += 1
                        if not self.flashing[line][column+1]: self.matrix[line][column+1] += 1
                        if not self.flashing[line+1][column+1]: self.matrix[line+1][column+1] += 1
                        if not self.flashing[line-1][column-1]: self.matrix[line-1][column-1] += 1
                        if not self.flashing[line+1][column-1]: self.matrix[line+1][column-1] += 1
                        if not self.flashing[line-1][column+1]: self.matrix[line-1][column+1] += 1
        # Reset the flashing matrix and see if they all flashed
        self.day += 1
        if all(self.flashing.flatten()) and not self.all_flashed:
            self.all_flashed = True
            self.day_all_flashed = self.day
        for line in range(10):
            for column in range(10):
                self.flashing[line][column] = False    
    def __str__(self): return str(self.matrix)


# Part 1
# TEST = 1656 | INPUT = 1739
octopus = Map(matrix)
for _ in range(100): octopus.update()
print('Part 1: ', octopus.total)
# Part 2
# TEST = 195 | INPUT = 324
while octopus.day_all_flashed == -1: octopus.update()
print('Part 2: ', octopus.day_all_flashed)

print('Time elapsed: ', time() - start)
