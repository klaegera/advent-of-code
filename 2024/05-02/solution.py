with open("input") as f:
    input = [line.strip() for line in f.readlines()]

from collections import Counter, defaultdict

it = iter(input)

g = defaultdict(set)
while line := next(it):
    a, b = line.split("|")
    g[a].add(b)


result = 0
while line := next(it, None):
    nodes = line.split(",")
    nodeset = set(nodes)
    subgraph = {a: g[a] & nodeset for a in nodeset}
    incoming = Counter(b for bs in subgraph.values() for b in bs)
    active = {n for n in subgraph if not incoming[n]}
    topo = []
    while active:
        n = active.pop()
        topo.append(n)
        for b in subgraph[n]:
            incoming[b] -= 1
            if not incoming[b]:
                active.add(b)
    if topo != nodes:
        result += int(topo[len(topo) // 2])

print(result)
