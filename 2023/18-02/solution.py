with open("input") as f:
    input = [line.strip() for line in f.readlines()]

steps = [("RDLU"[int(line[-2])], int(line[-7:-2], 16)) for line in input]


result = row = 0
for dir, dist in steps:
    match dir:
        case "U":
            row += dist
        case "D":
            row -= dist
        case "L":
            result += dist * row
        case "R":
            result -= dist * row

print(abs(result) + sum(dist for _, dist in steps) // 2 + 1)
