with open("input") as f:
    grid = [list(line.strip()) for line in f.readlines()]


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "^":
            guard = r, c
            break
    else:
        continue
    break


def simulate(guard, obstacle):
    visited = set()
    d = 0
    while True:
        if (guard, d) in visited:
            return True
        visited.add((guard, d))
        r, c = guard
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            return False
        while (nr, nc) == obstacle or grid[nr][nc] == "#":
            d += 1
            d %= 4
            dr, dc = dirs[d]
            nr, nc = r + dr, c + dc
        guard = nr, nc


result = 0
for r, row in enumerate(grid):
    print(r, "/", len(grid))
    for c, val in enumerate(row):
        if val == ".":
            result += simulate(guard, (r, c))

print(result)
