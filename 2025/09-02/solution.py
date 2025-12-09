with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

red = [tuple(map(int, line.split(","))) for line in lines]

result = 0
for i, (x1, y1) in enumerate(red):
    for x2, y2 in red[i + 1 :]:
        for (x3, y3), (x4, y4) in zip(red, red[1:] + red[:1]):
            if (
                max(x1, x2) > min(x3, x4)
                and min(x1, x2) < max(x3, x4)
                and max(y1, y2) > min(y3, y4)
                and min(y1, y2) < max(y3, y4)
            ):
                break
        else:
            result = max(result, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

print(result)
