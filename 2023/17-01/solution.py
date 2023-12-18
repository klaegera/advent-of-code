from heapq import heappush, heappop

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

city = [[int(v) for v in row] for row in input]


result = float("inf")
best = {}
check = [(0, 0, 0, None, 0)]


def update(cost, r, c, dir, speed):
    if not (0 <= r < len(city) and 0 <= c < len(city[0])) or speed > 3:
        return

    cost += city[r][c]

    if (r, c) == (len(city) - 1, len(city[0]) - 1):
        global result
        result = min(result, cost)
        return

    updated = False
    for s in range(speed, 4):
        key = r, c, dir, s
        if key not in best or cost < best[key]:
            best[key] = cost
            updated = True
    if updated:
        heappush(check, (cost, r, c, dir, speed))


while check:
    cost, r, c, dir, speed = heappop(check)

    if dir != "U":
        update(cost, r + 1, c, "D", speed + 1 if dir == "D" else 1)
    if dir != "D":
        update(cost, r - 1, c, "U", speed + 1 if dir == "U" else 1)
    if dir != "L":
        update(cost, r, c + 1, "R", speed + 1 if dir == "R" else 1)
    if dir != "R":
        update(cost, r, c - 1, "L", speed + 1 if dir == "L" else 1)

print(result)
