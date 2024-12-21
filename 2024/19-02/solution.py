with open("input") as f:
    input = [line.strip() for line in f.readlines()]

towels = input[0].split(", ")

from functools import cache


@cache
def dp(design):
    ways = design in towels
    for towel in towels:
        if design.startswith(towel):
            ways += dp(design[len(towel) :])
    return ways


result = sum(dp(design) for design in input[2:])
print(result)
