from bisect import insort
from collections import defaultdict, deque

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

blocks = sorted(
    (z1, (x1, x2), (y1, y2), z2 - z1 + 1)
    for x1, y1, z1, x2, y2, z2 in (
        map(int, line.replace("~", ",").split(",")) for line in input
    )
)


graph = defaultdict(list)
ingraph = defaultdict(list)
stacked = []

for i, (_, x, y, h) in enumerate(blocks):
    z = 0
    for (sz, sx, sy), si in stacked:
        if z and z != sz:
            break
        if x[0] <= sx[1] and sx[0] <= x[1] and y[0] <= sy[1] and sy[0] <= y[1]:
            z = sz
            graph[si].append(i)
            ingraph[i].append(si)
    insort(stacked, ((z - h, x, y), i))


result = 0
for base, supporting in graph.items():
    dropped = set([base])
    q = deque(dropped)
    while q:
        drop = q.popleft()
        if drop in graph:
            for block in graph[drop]:
                if block not in dropped and all(
                    sup in dropped for sup in ingraph[block]
                ):
                    dropped.add(block)
                    q.append(block)
                    result += 1

print(result)
