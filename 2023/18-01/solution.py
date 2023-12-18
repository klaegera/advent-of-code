with open("input") as f:
    input = [line.strip() for line in f.readlines()]

steps = [line.split() for line in input]


r, c = 0, 0
path = []

for dir, dist, _ in steps:
    for _ in range(int(dist)):
        path.append((r, c))
        match dir:
            case "U":
                r -= 1
            case "D":
                r += 1
            case "L":
                c -= 1
            case "R":
                c += 1

minr, minc = min(r for r, _ in path), min(c for _, c in path)
path = [(r - minr + 1, c - minc + 1) for r, c in path]
maxr, maxc = max(r for r, _ in path), max(c for _, c in path)

pathset = set(path)

flooded = set()
flood = [(0, 0)]
while flood:
    next = flood.pop()
    r, c = next
    if (
        0 <= r <= maxr + 1
        and 0 <= c <= maxc + 1
        and next not in flooded
        and next not in pathset
    ):
        flooded.add(next)
        flood.append((r - 1, c))
        flood.append((r + 1, c))
        flood.append((r, c - 1))
        flood.append((r, c + 1))

result = (maxr + 2) * (maxc + 2) - len(flooded)

print(result)


## To Visualize
# show = [["." for _ in range(maxc + 2)] for _ in range(maxr + 2)]
# for r, c in path:
#     show[r][c] = "#"
# for r, c in flooded:
#     show[r][c] = "~"
# for row in show:
#    print(row)
