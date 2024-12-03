with open("input") as f:
    input = f.read()

import re

enabled = True
result = 0
for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", input):
    if match[0] == "do()":
        enabled = True
    elif match[0] == "don't()":
        enabled = False
    elif enabled:
        result += int(match[1]) * int(match[2])

print(result)
