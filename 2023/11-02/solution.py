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

result = sum(
    2 * sum(i * v for i, v in enumerate(g)) - (len(g) - 1) * sum(g) for g in (gr, gc)
)

er = set(range(len(input))) - set(gr)
ec = set(range(len(input[0]))) - set(gc)

result += 999999 * sum(
    (x := bisect(g, v)) * (len(g) - x) for g, eg in ((gr, er), (gc, ec)) for v in eg
)

print(result)
