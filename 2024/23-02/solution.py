with open("input") as f:
    input = [line.strip() for line in f.readlines()]

from collections import defaultdict

g = defaultdict(set)

for line in input:
    a, b = line.split("-")
    g[a].add(b)
    g[b].add(a)

nodes = list(g)
out = set()


def foo(i, included, available):
    if i == len(nodes):
        out.add(",".join(sorted(included)))
        return
    n = nodes[i]
    if n in available:
        foo(i + 1, included | {n}, available & g[n])
    foo(i + 1, included, available)


foo(0, set(), g.keys())
print(max(out, key=len))
