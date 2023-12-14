import bisect

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in input[0][7:].split()]
seeds = [(start, length) for start, length in zip(seeds[::2], seeds[1::2])]

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


for map in maps:
    new_ranges = []
    while seeds:
        start, length = seeds.pop()
        new_start, new_length = start, length

        x = bisect.bisect(map, (start, float("inf"), float("inf")))

        if x > 0 and start < map[x - 1][1]:
            new_start = start - map[x - 1][0] + map[x - 1][2]
            new_length = min(length, map[x - 1][1] - start)
        elif x < len(map):
            new_length = min(length, map[x][0] - start)

        new_ranges.append((new_start, new_length))
        if new_length < length:
            seeds.append((start + new_length, length - new_length))
    seeds = new_ranges

print(min(seeds)[0])
