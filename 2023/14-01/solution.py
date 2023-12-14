with open("input") as f:
    input = [line.strip() for line in f.readlines()]


height = len(input)
cols = [[row[c] for row in input] for c in range(len(input[0]))]


result = 0
for col in cols:
    load = height
    for r, v in enumerate(col):
        match v:
            case "O":
                result += load
                load -= 1
            case "#":
                load = height - r - 1

print(result)
