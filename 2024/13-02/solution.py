with open("input") as f:
    input = [line.strip() for line in f.readlines()]

import re

result = 0
it = iter(input)
pattern = re.compile(r".*X.(\d+), Y.(\d+)")
while True:
    ax, ay = map(int, re.match(pattern, next(it)).groups())
    bx, by = map(int, re.match(pattern, next(it)).groups())
    px, py = map(int, re.match(pattern, next(it)).groups())
    px, py = px + 10000000000000, py + 10000000000000

    A = (by * px - bx * py) / (by * ax - bx * ay)
    B = (px - ax * A) / bx

    if A == int(A) and B == int(B):
        result += int(3 * A + B)

    if next(it, None) is None:
        break

print(result)
