from collections import Counter, defaultdict

TEST = 'test14.txt'
INPUT = 'input14.txt'

dicio = defaultdict(lambda: "")
count = Counter()

with open(TEST) as file: 
    polymer = list(file.readline().strip())
    _ = file.readline()
    rest = file.read().split('\n')
    # Separar
    for values in rest:
        left, right = values.split(' -> ')
        dicio[left] = right

def count(polymer, dicio, cicle):
    total = Counter(polymer)
    new_parts = Counter([polymer[i] + polymer[i + 1] for i in range(len(polymer) - 1)])

    for _ in range(cicle):
        new_parts, old_parts = Counter(), new_parts
        for (a, b), add in dicio.items():
            new = old_parts[a + b]
            if new:
                new_parts[a + add] += new
                new_parts[add + b] += new
                total[add] +=  new
    return total

# Part 1
# INPUT = 4244
result =  count(polymer, dicio, 40).most_common()
print('Part 2: ', result[0][1] - result[-1][1])
# print(count)
