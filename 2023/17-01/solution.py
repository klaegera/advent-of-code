from heapq import heappush, heappop

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

city = [[int(v) for v in row] for row in input]


best = {}


def update_best(cost, r, c, dir, speed, prev):
    updated = False
    for s in range(speed, 4):
        key = r, c, dir, s
        if key not in best or cost < best[key][0]:
            best[key] = cost, prev
            updated = True
    return updated


check = [(0, 0, 0, None, 0, None)]
while check:
    prev = heappop(check)
    cost, r, c, dir, speed, _ = prev

    if dir != "U" and r < len(city) - 1 and not (dir == "D" and speed == 3):
        next = (
            cost + city[r + 1][c],
            r + 1,
            c,
            "D",
            speed + 1 if dir == "D" else 1,
            prev,
        )
        if update_best(*next):
            heappush(check, next)
    if dir != "D" and r > 0 and not (dir == "U" and speed == 3):
        next = (
            cost + city[r - 1][c],
            r - 1,
            c,
            "U",
            speed + 1 if dir == "U" else 1,
            prev,
        )
        if update_best(*next):
            heappush(check, next)
    if dir != "L" and c < len(city[0]) - 1 and not (dir == "R" and speed == 3):
        next = (
            cost + city[r][c + 1],
            r,
            c + 1,
            "R",
            speed + 1 if dir == "R" else 1,
            prev,
        )
        if update_best(*next):
            heappush(check, next)
    if dir != "R" and c > 0 and not (dir == "L" and speed == 3):
        next = (
            cost + city[r][c - 1],
            r,
            c - 1,
            "L",
            speed + 1 if dir == "L" else 1,
            prev,
        )
        if update_best(*next):
            heappush(check, next)

result = float("inf")
for speed in range(1, 4):
    for dir in ("D", "R"):
        key = len(city) - 1, len(city[0]) - 1, dir, speed
        if key in best:
            result = min(result, best[key][0])

print(result)
