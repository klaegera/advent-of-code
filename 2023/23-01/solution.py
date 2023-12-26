from collections import defaultdict

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

compass = (-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")
h, w = len(input), len(input[0])
start, target = (1, 1), (h - 2, w - 2)

nodes = set((start, target))
for r in range(1, h - 1):
    for c in range(1, w - 1):
        if input[r][c] == ".":
            if sum(input[r + dr][c + dc] != "#" for dr, dc, _ in compass) != 2:
                nodes.add((r, c))


g = defaultdict(list)
for nr, nc in nodes:
    if (nr, nc) == target:
        continue
    for dr, dc, slope in compass:
        r, c = nr + dr, nc + dc
        if input[r][c] in (".", slope) and 0 < r < h - 1:
            steps = 1
            prev = nr, nc
            while (r, c) not in nodes:
                steps += 1
                for dr, dc, slope in compass:
                    next = r + dr, c + dc
                    if next != prev and input[next[0]][next[1]] in "." + slope:
                        prev = r, c
                        r, c = next
                        break
            g[nr, nc].append((steps, (r, c)))


result = 0

q = [(start, 2, set())]
while q:
    node, dist, visited = q.pop()
    for weight, neighbor in g[node]:
        if neighbor == target:
            result = max(result, dist + weight)
        elif neighbor not in visited:
            q.append((neighbor, dist + weight, visited | {neighbor}))

print(result)
