import numpy as np
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


maze = []
cost = []
with open(INPUT) as file:
    data = file.read().split('\n')
    for line in data:
        maze.append(list(map(int, line)))
        cost.append([-1] * len(line))
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
    

total_answer = search(maze,(0,0), cost)
print("Part 1:", total_answer)