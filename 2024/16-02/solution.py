with open("input") as f:
    input = [line.strip() for line in f.readlines()]


for r, row in enumerate(input):
    for c, val in enumerate(row):
        if val == "S":
            start = r, c
        if val == "E":
            end = r, c


from heapq import heappop, heappush

visited = {}
h = [(0, (start, (0, 1)), None)]
while h:
    score, pos, prev = heappop(h)
    if pos[0] == end:
        pos = end, (0, 0)
    if pos in visited:
        if visited[pos][0] == score:
            visited[pos][1].append(prev)
        elif pos[0] == end:
            break
        continue
    visited[pos] = score, [prev]
    (r, c), (dr, dc) = pos
    for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (ndr, ndc) == (-dr, -dc):
            continue
        nr, nc = r + ndr, c + ndc
        if input[nr][nc] == "#":
            continue
        if (ndr, ndc) == (dr, dc):
            heappush(h, (score + 1, ((nr, nc), (ndr, ndc)), pos))
        else:
            heappush(h, (score + 1000, ((r, c), (ndr, ndc)), pos))

backvisited = set()
q = [(end, (0, 0))]
while q:
    node = q.pop()
    if node is not None:
        backvisited.add(node[0])
        q.extend(visited[node][1])

print(len(backvisited))
