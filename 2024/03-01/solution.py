with open("input") as f:
    input = f.read()

import re

result = 0
for match in re.finditer(r"mul\((\d+),(\d+)\)", input):
    a, b = match.groups()
    result += int(a) * int(b)

print(result)
