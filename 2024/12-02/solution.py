with open("input") as f:
    input = [line.strip() for line in f.readlines()]

result = 0
visited = set()
for r, row in enumerate(input):
    for c, val in enumerate(row):
        if (r, c) not in visited:
            q = set([(r, c)])
            area = 0
            corners = 0
            while q:
                fr, fc = q.pop()
                visited.add((fr, fc))
                neighbors = 0
                ri, br, bo, bl, le, tl, to, tr = (
                    (
                        fr + dr,
                        fc + dc,
                        0 <= fr + dr < len(input)
                        and 0 <= fc + dc < len(input[0])
                        and input[fr + dr][fc + dc] == val,
                    )
                    for dr, dc in [
                        (0, 1),
                        (1, 1),
                        (1, 0),
                        (1, -1),
                        (0, -1),
                        (-1, -1),
                        (-1, 0),
                        (-1, 1),
                    ]
                )
                for nr, nc, match in (ri, bo, le, to):
                    if match:
                        neighbors += 1
                        if (nr, nc) not in visited:
                            q.add((nr, nc))
                for corner in [(ri, br, bo), (bo, bl, le), (le, tl, to), (to, tr, ri)]:
                    a, b, c = (x[2] for x in corner)
                    corners += (not a and not c) or (a and not b and c)
                area += 1
            result += area * corners

print(result)
