with open("input") as f:
    lines = [line.rstrip() for line in f.readlines()]

*lines, ops = lines
ops = [op for op in ops.split() if op]

from itertools import zip_longest, groupby

cols = ["".join(col).strip() for col in zip_longest(*lines, fillvalue="")]
nums = [list(g) for k, g in groupby(cols, bool) if k]

from math import prod

result = sum((sum if op == "+" else prod)(map(int, num)) for num, op in zip(nums, ops))

print(result)
