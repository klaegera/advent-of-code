with open("input") as f:
    input = f.readlines()

a, b = [], []
for line in input:
    x, y = map(int, line.split())
    a.append(x), b.append(y)

from collections import Counter

cb = Counter(b)

result = sum(n * cb[n] for n in a)

print(result)
