with open("input") as f:
    input = [line.strip() for line in f.readlines()]


def rot(table):
    return [[row[c] for row in table[::-1]] for c in range(len(table[0]))]


def roll(table):
    for row in table:
        space = 0
        for c, v in enumerate(row):
            if v == "O":
                row[c] = "."
                row[space] = "O"
                space += 1
            elif v == "#":
                space = c + 1
    return table


table = rot(rot(rot(input)))

seen = {}
seen_at = []

cycle = 0
while True:
    hashable = tuple(tuple(row) for row in table)
    if hashable in seen:
        seen_step = seen[hashable]
        break

    seen[hashable] = cycle
    seen_at.append(hashable)
    cycle += 1

    for _ in range(4):
        table = rot(roll(table))


i = seen_step + (1_000_000_000 - seen_step) % (cycle - seen_step)

result = sum(len(row) - c for row in seen_at[i] for c, v, in enumerate(row) if v == "O")

print(result)
