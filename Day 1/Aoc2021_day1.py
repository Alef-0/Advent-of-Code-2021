TEST = "input_test1.txt"
INPUT = "input1.txt"

with open(INPUT) as file: dephts = list(map(int,file.readlines()))

# Part 1
# TEST = 7 | INPUT = 1393
increased = 0
for i in range(1, len(dephts)):
    if dephts[i - 1] < dephts[i]: 
        increased += 1
print("Part 1: ", increased)

# Part 2
# TEST = 5 | INPUT = 1359
increased = 0
for i in range(1, len(dephts) - 3 + 1):
    if (dephts[i-1] + dephts[i] + dephts[i+1] < 
        dephts[i] + dephts[i+1] + dephts[i+2]): 
        increased += 1
print("Part 2: ", increased)