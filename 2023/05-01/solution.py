import bisect

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in input[0][7:].split()]

maps = [[]]
for line in input[2:]:
    if not line:
        maps.append([])
        continue
    if not line[0].isnumeric():
        continue
    dest, source, length = map(int, line.split())
    maps[-1].append((source, source + length, dest))

for map in maps:
    map.sort()


result = float("inf")

for seed in seeds:
    for map in maps:
        x = bisect.bisect_left(map, (seed, float("inf"), float("inf"))) - 1
        if x >= 0 and seed < map[x][1]:
            seed = seed - map[x][0] + map[x][2]
    result = min(result, seed)

print(result)
