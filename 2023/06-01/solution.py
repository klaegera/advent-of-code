import math

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

times = [int(t) for t in input[0].split()[1:]]
distances = [int(d) for d in input[1].split()[1:]]


result = 1
for t, d in zip(times, distances):
    q = t / 2
    r = math.sqrt(q**2 - d)
    result *= (
        math.floor(q + r)
        - math.ceil(q - r)
        + 1
        - (q + r == int(q + r))
        - (q - r == int(q - r))
    )

print(result)
