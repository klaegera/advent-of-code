with open("input") as f:
    input = [line.strip() for line in f.readlines()]

from collections import Counter

counter = Counter()
for line in input:
    secret = int(line)
    prices = [int(str(secret)[-1])]
    for _ in range(2000):
        secret ^= secret * 64
        secret %= 16777216
        secret ^= secret // 32
        secret %= 16777216
        secret ^= secret * 2048
        secret %= 16777216
        prices.append(int(str(secret)[-1]))
    diffs = tuple(b - a for a, b in zip(prices, prices[1:]))
    seqs = {}
    for i in range(len(diffs) - 4):
        key = diffs[i : i + 4]
        if key not in seqs:
            seqs[key] = prices[i + 4]
    counter += seqs

print(counter.most_common(1)[0][1])
