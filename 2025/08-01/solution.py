with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

boxes = [list(map(int, line.split(","))) for line in lines]

dist = []
for i, (x, y, z) in enumerate(boxes):
    for j, (x2, y2, z2) in enumerate(boxes[i + 1 :]):
        dist.append(((x - x2) ** 2 + (y - y2) ** 2 + (z - z2) ** 2, (i, i + 1 + j)))
dist.sort()

circuits = list(range(len(boxes)))


def find(i):
    if circuits[i] != i:
        circuits[i] = find(circuits[i])
    return circuits[i]


for _, (i, j) in dist[:1000]:
    circuits[find(j)] = find(i)

from collections import Counter

(_, a), (_, b), (_, c) = Counter(find(c) for c in circuits).most_common(3)

print(a * b * c)
