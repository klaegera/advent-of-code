with open("input") as f:
    input = [line.strip() for line in f.readlines()]

for r, row in enumerate(input):
    for c, val in enumerate(row):
        if val == "S":
            start = r, c
        elif val == "E":
            end = r, c


track = {}
r, c = start
t = 0
track[start] = 0
while (r, c) != end:
    t += 1
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        val = input[nr][nc]
        if val != "#" and (nr, nc) not in track:
            r, c = (nr, nc)
            track[(r, c)] = t
            break

C = 20

result = 0
for (r, c), t in track.items():
    for dr in range(-C, C + 1):
        x = C - abs(dr)
        for dc in range(-x, x + 1):
            cheat = r + dr, c + dc
            if cheat in track:
                saved = track[cheat] - t - (abs(dr) + abs(dc))
                if saved >= 100:
                    result += 1

print(result)
