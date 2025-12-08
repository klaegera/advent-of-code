with open("input") as f:
    vals = f.read().strip()

mults = [
    (int(("0" * n + "1") * m), 10**n, 10 ** (n + 1) - 1)
    for n in range(5)
    for m in range(2, 10 // (n + 1) + 1)
]

s = set()
for ab in vals.split(","):
    a, b = map(int, ab.split("-"))
    for m, l, r in mults:
        ma, mb = max(l, (a + m - 1) // m), min(r, b // m)
        for n in range(ma, mb + 1):
            s.add(n * m)

print(sum(s))
