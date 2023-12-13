with open("input") as f:
    input = [line.strip() for line in f.readlines()]


groups = [[]]
for row in input:
    if not row:
        groups.append([])
    else:
        groups[-1].append(row)


result = 0
for group in groups:
    for r in range(1, len(group)):
        if sum(a != b for pair in zip(group[r:], group[r - 1::-1]) for a, b in zip(*pair)) == 1:
            result += 100 * r
            break
    else:
        cols = ["".join(row[c] for row in group) for c in range(len(group[0]))]
        for c in range(1, len(cols)):
            if sum(a != b for pair in zip(cols[c:], cols[c - 1::-1]) for a, b in zip(*pair)) == 1:
                result += c
                break

print(result)
