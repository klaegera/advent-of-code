from functools import reduce

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

steps = input[0].split(",")

result = sum(reduce(lambda a, b: (a + ord(b)) * 17 % 256, step, 0) for step in steps)

print(result)
