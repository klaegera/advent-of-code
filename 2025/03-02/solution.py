with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
for line in lines:
    j = 0
    for k in range(11, -1, -1):
        n, i = max((n, -i) for i, n in enumerate(line[j : -k or None]))
        j += -i + 1
        result += int(n) * 10**k

print(result)
