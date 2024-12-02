with open("input") as f:
    input = f.readlines()

a, b = [], []
for line in input:
    x, y = map(int, line.split())
    a.append(x), b.append(y)

result = sum(abs(x - y) for x, y in zip(sorted(a), sorted(b)))

print(result)
