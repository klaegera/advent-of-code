with open("input") as f:
    input = [line.strip() for line in f.readlines()]

keys = []
locks = []

for i in range((len(input) + 1) // 8):
    top = i * 8
    cols = [0] * 5
    for row in input[top : top + 7]:
        for c in range(5):
            cols[c] += row[c] == "#"
    if input[top][0] == "#":
        locks.append(cols)
    else:
        keys.append(cols)

result = 0
for lock in locks:
    for key in keys:
        for l, k in zip(lock, key):
            if l + k > 7:
                break
        else:
            result += 1

print(result)
