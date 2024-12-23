with open("input") as f:
    input = [line.strip() for line in f.readlines()]

from collections import defaultdict

g = defaultdict(set)

for line in input:
    a, b = line.split("-")
    g[a].add(b)
    g[b].add(a)


out = set()
for a in g:
    if a[0] == "t":
        for b in g[a]:
            for c in g[b]:
                if a in g[c]:
                    out.add(tuple(sorted((a, b, c))))

print(len(out))
