from time import time_ns as time
from os.path import join, isfile

TEST = 'test17.txt'
INPUT = 'input17.txt'
LOCAL = 'Day 17'
CHOICE = INPUT
start = time()
if not isfile(CHOICE): CHOICE = join(LOCAL, CHOICE)

with open(CHOICE) as file:
    data = file.read().split()
    x = data[2][2:].removesuffix(',')
    y = data[3][2:].removesuffix(',')
    x = list(map(int,x.split('..')))
    y = list(map(int,y.split('..')))


def hit(x,y, velx, vely):
    posx, posy = 0,0
    limx1, limx2 = min(x), max(x)
    limy1, limy2 = min(y), max(y)
    while True:
        posx += velx
        posy += vely
        if limx1 <= posx <= limx2 and limy1 <= posy <= limy2:
            return True
        elif posx > limx2 or posy < limy1:
            return False
        
        if velx > 0: velx-=1
        elif velx<0: velx+=1
        vely -= 1

def brute_force(x,y):
    points = []
    # Don't care, change the maximum and minimums for better result
    # It's assumed it will never be -x
    for i in range(0, max(x)+1):
        for j in range(min(y), abs(min(y))+1):
            points.append((i,j))
    # See if it hits
    total = 0
    for point in points:
        if hit(x,y, point[0], point[1]):
            # print(point)
            total += 1
    return total

# PART 1 = 5995 | PART 2 = 3202
minimum = abs(min(y))
# Because it always comes back to zero with +1 of the original velocity in negative
print("Part 1: ", (minimum - 1) * minimum // 2)
# It takes almost a second, I don't even know how to optimize it
print("Part 2: ", brute_force(x,y))

print("Time elapsed in ns: ", time() - start)