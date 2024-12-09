with open("input") as f:
    input = [line.strip() for line in f.readlines()]

disk = []
for i, c in enumerate(input[0]):
    disk += [None if i % 2 else i // 2] * int(c)
n = sum(1 for c in disk if c is not None)

rev = (c for c in reversed(disk) if c is not None)

result = sum(i * (next(rev) if disk[i] is None else disk[i]) for i in range(n))

print(result)
