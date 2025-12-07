with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

beams = [0] * len(lines[0])
for line in lines:
    new_beams = beams.copy()
    for i, c in enumerate(line):
        match c:
            case "S":
                new_beams[i] = 1
            case "^":
                new_beams[i] = 0
                new_beams[i - 1] += beams[i]
                new_beams[i + 1] += beams[i]
    beams = new_beams

print(sum(beams))
