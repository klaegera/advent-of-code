with open("input") as f:
    input = [line.strip() for line in f.readlines()]

edges = []
it = iter(input)
while line := next(it):
    edges.append(line.split("|"))

result = 0
while line := next(it, None):
    elements = line.split(",")
    idx = {e: i for i, e in enumerate(elements)}
    for a, b in edges:
        if a in idx and b in idx and idx[a] > idx[b]:
            break
    else:
        result += int(elements[len(elements) // 2])

print(result)
