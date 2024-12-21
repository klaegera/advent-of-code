with open("input") as f:
    input = [line.strip() for line in f.readlines()]

towels = input[0].split(", ")

from functools import cache


@cache
def dp(design):
    if design in towels:
        return True
    for towel in towels:
        if design.startswith(towel) and dp(design[len(towel) :]):
            return True
    return False


result = sum(dp(design) for design in input[2:])
print(result)
