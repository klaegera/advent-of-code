with open("input") as f:
    input = [line.strip() for line in f.readlines()]

vals = {}

it = iter(input)
while line := next(it):
    k, v = line.split(": ")
    vals[k] = int(v)

from collections import defaultdict

downstream = defaultdict(list)
ops = {}
solvable = []

while line := next(it, None):
    a, op, b, _, c = line.split()
    ops[c] = a, op, b
    downstream[a].append(c)
    downstream[b].append(c)
    if a in vals and b in vals:
        solvable.append(c)

while solvable:
    c = solvable.pop()
    a, op, b = ops[c]
    vals[c] = int(
        vals[a] and vals[b]
        if op == "AND"
        else vals[a] or vals[b] if op == "OR" else vals[a] ^ vals[b]
    )
    for d in downstream[c]:
        a, _, b = ops[d]
        if a in vals and b in vals:
            solvable.append(d)

result = int(
    "".join(str(vals[k]) for k in sorted(vals, reverse=True) if k[0] == "z"), base=2
)

print(result)
