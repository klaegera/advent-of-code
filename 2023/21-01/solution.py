with open("input") as f:
    input = [line.strip() for line in f.readlines()]

plots = set()
for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c] != "#":
            plots.add((r, c))
            if input[r][c] == "S":
                start = (r, c)


steps = ((1, 0), (-1, 0), (0, 1), (0, -1))

reachable = set((start,))
for _ in range(64):
    next_reachable = set()
    for r, c in reachable:
        for dr, dc in steps:
            next_reachable.add((r + dr, c + dc))
    reachable = next_reachable & plots

print(len(reachable))
