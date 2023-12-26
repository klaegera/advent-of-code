from collections import defaultdict
from random import choices
from math import prod

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

graph = defaultdict(list)

for line in input:
    a, bs = line.split(": ")
    for b in bs.split():
        graph[a].append(b)
        graph[b].append(a)


while True:
    g = graph
    while len(g) > 2:
        node = choices(list(g.keys()), weights=map(len, g.values()))[0]
        edge = choices(g[node])[0]
        g = {
            (node + edge): [
                e for n in (node, edge) for e in g[n] if e not in (node, edge)
            ]
        } | {
            n: [node + edge if e in (node, edge) else e for e in g[n]]
            for n in g
            if n not in (node, edge)
        }
    if len(next(iter(g.values()))) == 3:
        print(prod(len(n) // 3 for n in g))
        break
