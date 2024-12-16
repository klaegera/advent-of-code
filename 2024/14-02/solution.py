with open("input") as f:
    input = [line.strip() for line in f.readlines()]

w, h = 101, 103

import re

robots = []
pattern = re.compile(r"p=(.+),(.+) v=(.+),(.+)")
for line in input:
    robots.append([int(x) for x in re.match(pattern, line).groups()])

from collections import Counter

# x-axis alignment
p = max(
    (Counter((px + i * vx) % w for px, _, vx, _ in robots).most_common(1)[0][1], i)
    for i in range(w)
)[1]

# y-axis alignment
q = max(
    (Counter((py + i * vy) % h for _, py, _, vy in robots).most_common(1)[0][1], i)
    for i in range(h)
)[1]

### calculation:
# m * w + p = n * h + q = result
# m = (n * h + q - p) / w
# n * h + q - p = 0 mod w
# n = (p - q) * (h ^ -1) mod w

n = ((p - q) * pow(h, -1, w)) % w
result = n * h + q

tree = set(
    ((px + result * vx) % w, (py + result * vy) % h) for px, py, vx, vy in robots
)
for r in range(h):
    print("".join("#" if (c, r) in tree else "." for c in range(w)))

print(result)
