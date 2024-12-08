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
            for dir in (1, -1):
                t = 0
                while True:
                    ar, ac = r1 + dir * t * dr, c1 + dir * t * dc
                    if not (0 <= ar < len(input) and 0 <= ac < len(input[0])):
                        break
                    anti.add((ar, ac))
                    t += 1

print(len(anti))
