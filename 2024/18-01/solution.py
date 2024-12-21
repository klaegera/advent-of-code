with open("input") as f:
    input = [line.strip() for line in f.readlines()]

bytes = [(int(r), int(c)) for c, r in (line.split(",") for line in input)]

N = 71
grid = [[False] * N for _ in range(N)]

for r, c in bytes[:1024]:
    grid[r][c] = True

from collections import deque

q = deque([((0, 0), 0)])
visited = set()
while q:
    (r, c), steps = q.popleft()
    if (r, c) == (N - 1, N - 1):
        print(steps)
        break
    if (r, c) in visited:
        continue
    visited.add((r, c))
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and not grid[nr][nc]:
            q.append(((nr, nc), steps + 1))
