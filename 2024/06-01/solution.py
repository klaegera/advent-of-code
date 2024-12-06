with open("input") as f:
    grid = [list(line.strip()) for line in f.readlines()]


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "^":
            break
    else:
        continue
    break

while True:
    grid[r][c] = "X"
    dr, dc = dirs[d]
    nr, nc = r + dr, c + dc
    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
        break
    while grid[nr][nc] == "#":
        d += 1
        d %= 4
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
    r, c = nr, nc

result = sum(val == "X" for row in grid for val in row)

print(result)
