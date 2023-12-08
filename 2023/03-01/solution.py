import re
import bisect

with open("input") as f:
    input = f.readlines()

symbols = [
    [i for i, s in enumerate(line.strip()) if not s.isnumeric() and s != "."]
    for line in input
]

result = 0

number_regex = re.compile(r"\d+")
for i, line in enumerate(input):
    for match in number_regex.finditer(line):
        l, r = match.start() - 1, match.end() + 1
        for symbol_line in symbols[max(i - 1, 0) : min(i + 2, len(symbols))]:
            x = bisect.bisect_left(symbol_line, l)
            if x < len(symbol_line) and symbol_line[x] < r:
                result += int(match.group())
                break

print(result)
