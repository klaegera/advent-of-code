with open("input") as f:
    input = [line.strip() for line in f.readlines()]

antennas = {}
for r, row in enumerate(input):
    for c, val in enumerate(row):
        if val != ".":
            antennas[val] = antennas.get(val, list()) + [(r, c)]

anti = set()
for group in antennas.values():
    for i, (r1, c1) in enumerate(group):
        for r2, c2 in group[i + 1 :]:
            dr, dc = r2 - r1, c2 - c1
            for ar, ac in ((r1 - dr, c1 - dc), (r2 + dr, c2 + dc)):
                if 0 <= ar < len(input) and 0 <= ac < len(input[0]):
                    anti.add((ar, ac))

print(len(anti))
