with open("input") as f:
    input = [line.strip() for line in f.readlines()]

elves = []

it = iter(input)
while True:
    elf = 0
    while line := next(it, None):
        elf += int(line)
    elves.append(elf)
    if line is None:
        break

print(sum(sorted(elves)[-3:]))
