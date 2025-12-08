with open("input") as f:
    vals = f.read().strip()

s = 0
for ab in vals.split(","):
    a, b = ab.split("-")
    q = 10 ** (len(b) // 2) + 1
    a, b = int(a), int(b)
    ma, mb = (a + q - 1) // q, b // q
    ma, mb = max(ma, q // 10), min(mb, q - 2)
    if mb >= ma:
        s += (ma + mb) * (mb - ma + 1) // 2 * q

print(s)
