iv = []

with open("input") as f:
    while line := f.readline().strip():
        iv.append(list(map(int, line.split("-"))))

iv.sort()

j = None
for i, (a, b) in enumerate(iv):
    if j is not None and a <= iv[j][1] + 1:
        print(i, a, b)
        iv[j][1] = max(iv[j][1], b)
        iv[i] = None
    else:
        j = i
iv = list(filter(None, iv))

result = sum(b - a + 1 for a, b in iv)

print(result)
