with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
for line in lines:
    n, i = max((n, -i) for i, n in enumerate(line[:-1]))
    result += int(n + max(line[-i + 1 :]))

print(result)
