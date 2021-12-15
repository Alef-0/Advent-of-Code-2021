import numpy as np
from os.path import isfile, join
from time import time_ns as time
from sys import maxsize

class point():
    def __init__(self, line, column, cost):
        self.line = line
        self.column = column
        self.cost = cost
    
    def __repr__(self):
        return f'({self.line},{self.column}) = {self.cost}'

class heap():
    def __init__(self, line, column, cost):
        self.queue : list = []
        self.queue.append(point(line,column, cost))
    
    def __str__(self):
        return str(self.queue)

    def add_heap(self, line, column, cost):
        self.queue.insert(0, point(line,column, cost))
        self.heapifying(0)

    def pop(self):
        return_value = self.queue.pop(0)
        if self.not_empty():
            self.queue.insert(0,self.queue.pop())
            self.heapifying(0)
        return return_value.line, return_value.column, return_value.cost

    def heapifying(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.queue) and self.queue[left].cost < self.queue[index].cost:
            self.queue[left], self.queue[index] = self.queue[index], self.queue[left]
            self.heapifying(left)
        if right < len(self.queue) and self.queue[right].cost < self.queue[index].cost:
            self.queue[right], self.queue[index] = self.queue[index], self.queue[right]
            self.heapifying(right)
    
    def not_empty(self):
        return len(self.queue) > 0

TEST = 'test15.txt'
INPUT = 'input15.txt'
start = time()
LOCAL = 'Day 15'
CHOICE = INPUT
if not isfile(CHOICE): CHOICE = join(LOCAL, CHOICE)


maze = []
cost = []
with open(CHOICE) as file:
    data = file.read().split('\n')
    for line in data:
        maze.append(list(map(int, line)))
        cost.append([-1] * len(line))
    original_maze = maze.copy()
    maze = np.array(maze)
    cost = np.array(cost)

# print(maze)
# print(cost)
max = len(maze)
cost[0,0] =  0
maze[0,0] =  0 
end = (len(maze)-1, len(maze[0])-1)

def search(maze, start, cost):
    queue = heap(start[0], start[1], cost[start])
    visited = set()
    while queue.not_empty():
        line, column, weight = queue.pop()
        visited.add((line, column))
        for x, y in ([1,0], [0,1], [-1,0], [0,-1]):
            node = (line + x, column + y)
            if 0 <= node[0] < max and 0 <= node[1] < max and node not in visited:
                if weight + maze[node] < cost[node] or cost[node] == -1:
                    cost[node] = weight + maze[node]
                    queue.add_heap(node[0], node[1], cost[node])
    return cost[end]
    
# PART 1
# TEST = 40 | INPUT = 537
total_answer = search(maze,(0,0), cost)
print("Part 1:", total_answer)

# PART 2
# TEST = 315 | INPUT = 2881
def expand(maze, size):
    # Create 5 new iterations of arrays
    maze_copies = [[] for _ in range(size * 5)]
    # Make copies by adding the original line 5 times
    for i in range(size*5):
        for _ in range(5):
            maze_copies[i] += maze[i % size].copy()
    
    # Change values
    for line in range(size * 5):
        for column in range(size * 5):
            maze_copies[line][column] = (maze_copies[line][column]  + (line // size) + (column // size))
            if maze_copies[line][column] > 9: maze_copies[line][column] %= 9 # Because it loops from 9 to 1
    #
    return np.array(maze_copies)

new_maze = expand(original_maze, len(maze))
cost = np.array([[-1 for _ in range(len(new_maze))] for _ in range(len(new_maze))])

cost[0,0] =  0
new_maze[0,0] =  0 

end = (len(new_maze)-1, len(new_maze[0])-1)
max = len(new_maze)
total_answer = search(new_maze, (0,0), cost)

print("Part 2:", total_answer)
print('Time elapsed in ns: ', time() - start)