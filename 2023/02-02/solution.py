with open("input") as f:
    input = f.readlines()


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

    minset = {"red": 0, "green": 0, "blue": 0}

    for draw in draws:
        for k, v in draw.items():
            minset[k] = max(minset[k], v)

    result += minset["red"] * minset["green"] * minset["blue"]

print(result)
