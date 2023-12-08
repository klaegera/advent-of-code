with open("input") as f:
    input = [line.strip() for line in f.readlines()]

cards = [
    [part.split() for part in line.split(":")[1][1:].split(" | ")] for line in input
]

counts = [1 for _ in cards]

for i, (winning, have) in enumerate(cards):
    n = len(set(winning) & set(have))
    for j in range(i + 1, min(i + 1 + n, len(counts))):
        counts[j] += counts[i]

print(sum(counts))
