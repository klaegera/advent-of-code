with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

from itertools import combinations

result = 0
for line in lines:
    target, *buttons, _ = line.split()
    target = int(target[-2:0:-1].replace("#", "1").replace(".", "0"), 2)
    buttons = [sum(2 ** int(l) for l in r[1:-1].split(",")) for r in buttons]

    for r in range(len(buttons)):
        for comb in combinations(buttons, r):
            lights = 0
            for button in comb:
                lights ^= button
            if lights == target:
                result += r
                break
        else:
            continue
        break

print(result)
