import re
import bisect

with open("input") as f:
    input = f.readlines()

symbols = [[i for i, s in enumerate(line.strip()) if s == "*"] for line in input]

result = 0

ratios = [[[] for _ in line] for line in symbols]

number_regex = re.compile(r"\d+")
for i, line in enumerate(input):
    for match in number_regex.finditer(line):
        l, r = match.start() - 1, match.end() + 1
        for j in range(max(i - 1, 0), min(i + 2, len(symbols))):
            symbol_line = symbols[j]
            x = bisect.bisect_left(symbol_line, l)
            if x < len(symbol_line) and symbol_line[x] < r:
                ratios[j][x].append(int(match.group()))

result = sum(
    ratio[0] * ratio[1] for line in ratios for ratio in line if len(ratio) == 2
)

print(result)
