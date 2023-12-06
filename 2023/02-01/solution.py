with open("input") as f:
    input = f.readlines()


limits = {"red": 12, "green": 13, "blue": 14}

result = 0

for line in input:
    game, draws = line.split(": ")
    gamenum = int(game[5:])
    draws = [
        {
            singledraw.split()[1]: int(singledraw.split()[0])
            for singledraw in draw.split(", ")
        }
        for draw in draws.split("; ")
    ]

    for draw in draws:
        for k, v in draw.items():
            if v > limits[k]:
                break
        else:
            continue
        break
    else:
        result += gamenum

print(result)
