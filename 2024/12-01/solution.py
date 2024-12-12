with open("input") as f:
    input = [line.strip() for line in f.readlines()]

result = 0
visited = set()
for r, row in enumerate(input):
    for c, val in enumerate(row):
        if (r, c) not in visited:
            q = set([(r, c)])
            area = 0
            perimeter = 0
            while q:
                fr, fc = q.pop()
                visited.add((fr, fc))
                neighbors = 0
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr, nc = fr + dr, fc + dc
                    if (
                        0 <= nr < len(input)
                        and 0 <= nc < len(input[0])
                        and input[nr][nc] == val
                    ):
                        neighbors += 1
                        if (nr, nc) not in visited:
                            q.add((nr, nc))
                area += 1
                perimeter += 4 - neighbors
            result += area * perimeter

print(result)
