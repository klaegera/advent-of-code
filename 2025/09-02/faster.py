with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

red = [tuple(map(int, line.split(","))) for line in lines]

lines = [
    ((min(x3, x4), min(y3, y4)), (max(x3, x4), max(y3, y4)))
    for (x3, y3), (x4, y4) in zip(red, red[1:] + red[:1])
]

result = 0
for i, (x1, y1) in enumerate(red):
    for x2, y2 in red[i + 1 :]:
        minx, maxx, miny, maxy = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
        for (minx2, miny2), (maxx2, maxy2) in lines:
            if maxx > minx2 and minx < maxx2 and maxy > miny2 and miny < maxy2:
                break
        else:
            result = max(result, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

print(result)
