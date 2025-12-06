with open("input") as f:
    lines = f.readlines()

lines = [[x for x in line.split() if x] for line in lines]

from math import prod

result = sum((sum if op == "+" else prod)(map(int, nums)) for *nums, op in zip(*lines))

print(result)
