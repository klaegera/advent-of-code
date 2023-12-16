from bisect import bisect

with open("input") as f:
    input = [line.strip() for line in f.readlines()]


gr, gc = [], []

for r, row in enumerate(input):
    for c, val in enumerate(row):
        if val == "#":
            gr.append(r)
            gc.append(c)

gc.sort()


result = 0
for g in (gr, gc):
    result += sum(v * (2 * i - len(g) + 1) for i, v in enumerate(g))
    empty = set(range(g[-1])) - set(g)
    result += sum((x := bisect(g, v)) * (len(g) - x) for v in empty)

print(result)
