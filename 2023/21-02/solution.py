with open("input") as f:
    input = [line.strip() for line in f.readlines()]

s = len(input)
plots = set()
for r in range(s):
    for c in range(s):
        if input[r][c] != "#":
            plots.add((r, c))
            if input[r][c] == "S":
                start = (r, c)


poly = []
steps = ((1, 0), (-1, 0), (0, 1), (0, -1))
active, reachable = set((start,)), set()
for i in range(s * 5 // 2 + 1):
    next = set()
    for r, c in active:
        for dr, dc in steps:
            p = r + dr, c + dc
            if (p[0] % s, p[1] % s) in plots and not p in reachable:
                next.add(p)
                reachable.add(p)
    active = next
    if i % s == s // 2:
        poly.append(sum((r + c) % 2 == (len(poly) + 1) % 2 for r, c in reachable))

v1, v2, v3 = poly
n = 26501365 // s
result = v1 + n * (v2 - v1) + (n - 1) * n // 2 * (v3 - 2 * v2 + v1)

print(result)
