with open("input") as f:
    input = [line.strip() for line in f.readlines()]


it = iter(input)

grid = []
while line := next(it):
    if "@" in line:
        r, c = len(grid), line.index("@")
        line = line.replace("@", ".")
    grid.append(list(line))

dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

while line := next(it, None):
    for dir in line:
        dr, dc = dirs[dir]
        i = 1
        while True:
            match grid[r + i * dr][c + i * dc]:
                case "#":
                    break
                case ".":
                    for j in range(i, 1, -1):
                        grid[r + j * dr][c + j * dc] = "O"
                        grid[r + (j - 1) * dr][c + (j - 1) * dc] = "."
                    r, c = r + dr, c + dc
                    break
            i += 1

result = 0
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "O":
            result += 100 * r + c

print(result)
