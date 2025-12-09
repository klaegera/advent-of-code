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


num = len(circuits)
for _, (i, j) in dist:
    if find(i) != find(j):
        num -= 1
        if num == 1:
            print(boxes[i][0] * boxes[j][0])
            break
    circuits[find(j)] = find(i)
