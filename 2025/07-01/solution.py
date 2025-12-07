with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

beams = set()
splits = 0
for line in lines:
    for i, c in enumerate(line):
        match c:
            case "S":
                beams.add(i)
            case "^":
                if i in beams:
                    beams.remove(i)
                    beams.add(i - 1)
                    beams.add(i + 1)
                    splits += 1

print(splits)
