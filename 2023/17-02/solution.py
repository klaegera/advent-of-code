from heapq import heappush, heappop

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

city = [[int(v) for v in row] for row in input]


result = float("inf")
best = {}
check = [(0, 0, 0, None, 4)]


def update(cost, r, c, dir, speed):
    if not (0 <= r < len(city) and 0 <= c < len(city[0])) or speed > 10:
        return

    cost += city[r][c]

    if (r, c) == (len(city) - 1, len(city[0]) - 1) and speed >= 4:
        global result
        result = min(result, cost)
        return

    key = r, c, dir, speed
    if key not in best or cost < best[key]:
        best[key] = cost
        heappush(check, (cost, r, c, dir, speed))


while check:
    cost, r, c, dir, speed = heappop(check)

    if dir != "U" and (dir == "D" or speed >= 4):
        update(cost, r + 1, c, "D", speed + 1 if dir == "D" else 1)
    if dir != "D" and (dir == "U" or speed >= 4):
        update(cost, r - 1, c, "U", speed + 1 if dir == "U" else 1)
    if dir != "L" and (dir == "R" or speed >= 4):
        update(cost, r, c + 1, "R", speed + 1 if dir == "R" else 1)
    if dir != "R" and (dir == "L" or speed >= 4):
        update(cost, r, c - 1, "L", speed + 1 if dir == "L" else 1)

print(result)
