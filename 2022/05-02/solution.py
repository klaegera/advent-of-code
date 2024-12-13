with open("input") as f:
    input = [line.rstrip() for line in f.readlines()]

from itertools import zip_longest
import re


it = iter(input)
pattern = re.compile(r"\[(.)\]|    ")
rows = []
while True:
    row = re.findall(pattern, next(it))
    if not row:
        next(it)
        break
    rows.append(row)

stacks = [
    [block for block in stack if block]
    for stack in zip_longest(*reversed(rows), fillvalue="")
]

pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
while line := next(it, None):
    num, src, dst = map(int, re.match(pattern, line).groups())
    stacks[dst - 1].extend(stacks[src - 1][-num:])
    del stacks[src - 1][-num:]


print("".join(stack[-1] for stack in stacks))
