with open("input") as f:
    input = [line.strip() for line in f.readlines()]

vals = "ABCXYZ"

result = 0
for line in input:
    op, end = map(lambda x: vals.index(x), line.split())
    result += (op + end + 2) % 3 + 1 + end % 3 * 3

print(result)
