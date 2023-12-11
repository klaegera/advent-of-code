with open("input") as f:
    input = [line.strip() for line in f.readlines()]


for r, row in enumerate(input):
    for c, pipe in enumerate(row):
        if pipe == "S":
            break
    else:
        continue
    break


result = 0
dir = None
while not dir or input[r][c] != "S":
    result += 1
    if dir != "D" and r and input[r][c] in ("SL|J") and input[r - 1][c] in ("S7|F"):
        r -= 1
        dir = "U"
    elif (
        dir != "L"
        and c < len(input[0]) - 1
        and input[r][c] in ("SF-L")
        and input[r][c + 1] in ("SJ-7")
    ):
        c += 1
        dir = "R"
    elif (
        dir != "U"
        and r < len(input) - 1
        and input[r][c] in ("S7|F")
        and input[r + 1][c] in ("SL|J")
    ):
        r += 1
        dir = "D"
    else:
        c -= 1
        dir = "L"

print(result // 2)
