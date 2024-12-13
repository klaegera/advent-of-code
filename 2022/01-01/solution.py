with open("input") as f:
    input = [line.strip() for line in f.readlines()]

result = 0

it = iter(input)
while True:
    elf = 0
    while line := next(it, None):
        elf += int(line)
    result = max(result, elf)
    if line is None:
        break

print(result)
