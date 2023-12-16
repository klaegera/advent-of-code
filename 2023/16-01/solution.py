with open("input") as f:
    input = [line.strip() for line in f.readlines()]


check = [(0, 0, "R")]
checked = set(check)

while check:
    r, c, dir = check.pop()
    match input[r][c], dir:
        case "/", "R":
            dir = "U"
        case "/", "D":
            dir = "L"
        case "/", "L":
            dir = "D"
        case "/", "U":
            dir = "R"
        case "\\", "R":
            dir = "D"
        case "\\", "D":
            dir = "R"
        case "\\", "L":
            dir = "U"
        case "\\", "U":
            dir = "L"
        case "-", ("D" | "U"):
            dir = "LR"
        case "|", ("L" | "R"):
            dir = "UD"
    for d in dir:
        match d:
            case "R":
                c += 1
            case "D":
                r += 1
            case "L":
                c -= 1
            case "U":
                r -= 1
        if 0 <= r < len(input) and 0 <= c < len(input[0]) and (r, c, d) not in checked:
            check.append((r, c, d))
            checked.add((r, c, d))

result = len(set((r, c) for r, c, _ in checked))

print(result)
