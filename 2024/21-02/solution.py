with open("input") as f:
    input = [line.strip() for line in f.readlines()]

pad = "789 456 123 _0A <v>"
coords = {"^": (3, 1)}
for r, row in enumerate(pad.split()):
    for c, val in enumerate(row):
        coords[val] = r, c

from functools import cache


@cache
def dp(prev, depth):
    if not depth:
        return len(prev)

    result = 0
    r, c = coords["A"]
    for val in prev:
        seq = ""
        nr, nc = coords[val]
        dr, dc = nr - r, nc - c
        if dr < 0:
            seq += "^" * -dr
        else:
            seq += "v" * dr
        if dc < 0:
            seq += "<" * -dc
        else:
            seq += ">" * dc

        result += min(
            dp(seq + "A", depth - 1) if (nr, c) != coords["_"] else float("inf"),
            dp(seq[::-1] + "A", depth - 1) if (r, nc) != coords["_"] else float("inf"),
        )

        r, c = nr, nc

    return result


result = sum(dp(line, 26) * int(line[:-1]) for line in input)

print(result)
