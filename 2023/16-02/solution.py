with open("input") as f:
    input = [line.strip() for line in f.readlines()]


result = 0

rowstarts = sum(
    [[(r, 0, "R"), (r, len(input[0]) - 1, "L")] for r in range(len(input))], []
)
colstarts = sum(
    [[(0, c, "D"), (len(input) - 1, c, "U")] for c in range(len(input[0]))], []
)

for start in rowstarts + colstarts:
    check = [start]
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
            if (
                0 <= r < len(input)
                and 0 <= c < len(input[0])
                and (r, c, d) not in checked
            ):
                check.append((r, c, d))
                checked.add((r, c, d))

    result = max(result, len(set((r, c) for r, c, _ in checked)))

print(result)
