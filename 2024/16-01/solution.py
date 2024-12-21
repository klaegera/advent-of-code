with open("input") as f:
    input = [line.strip() for line in f.readlines()]


for r, row in enumerate(input):
    for c, val in enumerate(row):
        if val == "S":
            start = r, c


from heapq import heappop, heappush

visited = set()
h = [(0, start, (0, 1))]
while h:
    score, (r, c), (dr, dc) = heappop(h)
    if (r, c) in visited:
        continue
    visited.add((r, c))
    match input[r][c]:
        case "E":
            print(score)
            break
        case "#":
            continue
    for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        heappush(
            h,
            (
                score + (1 if (ndr, ndc) == (dr, dc) else 1001),
                (r + ndr, c + ndc),
                (ndr, ndc),
            ),
        )
