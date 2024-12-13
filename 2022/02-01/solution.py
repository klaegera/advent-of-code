with open("input") as f:
    input = [line.strip() for line in f.readlines()]

vals = "ABCXYZ"

result = 0
for line in input:
    op, me = map(lambda x: vals.index(x), line.split())
    result += me % 3 + 1 + (me - op + 1) % 3 * 3

print(result)
