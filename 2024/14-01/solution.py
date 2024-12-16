with open("input") as f:
    input = [line.strip() for line in f.readlines()]

w, h = 101, 103

import re

quadrants = [0] * 4
pattern = re.compile(r"p=(.+),(.+) v=(.+),(.+)")
for line in input:
    px, py, vx, vy = map(int, re.match(pattern, line).groups())
    x, y = (px + 100 * vx) % w, (py + 100 * vy) % h
    if x < w // 2 and y < h // 2:
        quadrants[0] += 1
    elif x < w // 2 and y > h // 2:
        quadrants[1] += 1
    elif x > w // 2 and y < h // 2:
        quadrants[2] += 1
    elif x > w // 2 and y > h // 2:
        quadrants[3] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
