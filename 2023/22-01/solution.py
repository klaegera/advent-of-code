from bisect import insort

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

blocks = sorted(
    (z1, (x1, x2), (y1, y2), z2 - z1 + 1)
    for x1, y1, z1, x2, y2, z2 in (
        map(int, line.replace("~", ",").split(",")) for line in input
    )
)


unremovable = set()
stacked = []

for _, x, y, h in blocks:
    z = 0
    touching = None
    for sz, sx, sy in stacked:
        if z and z != sz:
            break
        if x[0] <= sx[1] and sx[0] <= x[1] and y[0] <= sy[1] and sy[0] <= y[1]:
            if z:
                touching = None
                break
            z = sz
            touching = (sx, sy, sz)
    if touching:
        unremovable.add(touching)
    insort(stacked, (z - h, x, y))

print(len(blocks) - len(unremovable))
