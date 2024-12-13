with open("input") as f:
    input = [line.strip() for line in f.readlines()]

import re

pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

result = 0
for line in input:
    a, b, c, d = map(int, re.match(pattern, line).groups())
    result += a <= c and b >= c or c <= a and d >= a

print(result)
