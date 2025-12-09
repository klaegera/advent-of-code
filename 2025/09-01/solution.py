with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

red = [tuple(map(int, line.split(","))) for line in lines]

result = 0
for i, (x1, y1) in enumerate(red):
    for x2, y2 in red[i + 1 :]:
        result = max(result, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

print(result)
