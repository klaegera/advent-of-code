with open("input") as f:
    input = [line.strip() for line in f.readlines()]

it = iter(input)

grid = []
while line := next(it):
    grid.append([])
    for v in line:
        match v:
            case "@":
                r, c = len(grid) - 1, len(grid[-1])
                grid[-1].extend("..")
            case "#":
                grid[-1].extend("##")
            case "O":
                grid[-1].extend("[]")
            case ".":
                grid[-1].extend("..")

dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
while line := next(it, None):
    for d in line:
        dr, dc = dirs[d]
        to_push = [(r + dr, c + dc)]
        i = 0
        while i < len(to_push):
            pr, pc = to_push[i]
            i += 1
            match grid[pr][pc]:
                case "#":
                    break
                case "[":
                    if (pr, pc + 1) not in to_push:
                        to_push.append((pr, pc + 1))
                case "]":
                    if (pr, pc - 1) not in to_push:
                        to_push.append((pr, pc - 1))
                case ".":
                    continue
            if (pr + dr, pc + dc) not in to_push:
                to_push.append((pr + dr, pc + dc))
        else:
            for pr, pc in reversed(to_push):
                if grid[pr][pc] != ".":
                    grid[pr + dr][pc + dc] = grid[pr][pc]
                    grid[pr][pc] = "."
            r, c = r + dr, c + dc


result = 0
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "[":
            result += 100 * r + c

print(result)
