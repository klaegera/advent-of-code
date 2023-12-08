with open("input") as f:
    input = [line.strip() for line in f.readlines()]

cards = [
    [part.split() for part in line.split(":")[1][1:].split(" | ")] for line in input
]

result = 0
for winning, have in cards:
    n = len(set(winning) & set(have))
    if n:
        result += 2 ** (n - 1)

print(result)
