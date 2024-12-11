with open("input") as f:
    input = [line.strip() for line in f.readlines()]

stones = input[0].split()

from collections import Counter

c = Counter(stones)
for _ in range(75):
    next_c = Counter()
    for stone, count in c.items():
        if stone == "0":
            next_c["1"] += count
        elif len(stone) % 2 == 0:
            next_c[stone[: len(stone) // 2]] += count
            next_c[str(int(stone[len(stone) // 2 :]))] += count
        else:
            next_c[str(2024 * int(stone))] += count
    c = next_c


print(sum(c.values()))
