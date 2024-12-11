with open("input") as f:
    input = [line.strip() for line in f.readlines()]

stones = input[0].split()
next_stones = []
for _ in range(25):
    for stone in stones:
        if stone == "0":
            next_stones += ["1"]
        elif len(stone) % 2 == 0:
            next_stones += [
                stone[: len(stone) // 2],
                str(int(stone[len(stone) // 2 :])),
            ]
        else:
            next_stones += [str(2024 * int(stone))]
    stones, next_stones = next_stones, []

print(len(stones))
