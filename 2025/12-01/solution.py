with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

# observation: the blocks always either do not fit at all
# (based on area), or fit trivially, with hundreds to spare

block_sizes = [7, 7, 7, 6, 5, 7]

result = 0
for line in lines[30:]:
    grid, *blocks = line.split()
    x, y = grid[:-1].split("x")
    result += int(x) * int(y) >= sum(int(c) * bs for c, bs in zip(blocks, block_sizes))

print(result)
