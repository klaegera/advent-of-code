with open("input") as f:
    input = [line.strip() for line in f.readlines()]

from heapq import heappush, heappop

files = []
spaces = [[] for _ in range(10)]
block = 0
for i, c in enumerate(input[0]):
    size = int(c)
    if i % 2:
        heappush(spaces[size], block)
    else:
        files.append([block, i // 2, size])
    block += size

for file in reversed(files):
    file_block, _, file_size = file
    space_block, space_size = min(
        ((spaces[size][0], size) for size in range(file_size, 10) if spaces[size]),
        default=(None, None),
    )
    if space_block is None or space_block > file_block:
        continue
    file[0] = space_block
    heappop(spaces[space_size])
    heappush(spaces[space_size - file_size], space_block + file_size)

result = sum(id * (block + block + size - 1) * size // 2 for block, id, size in files)

print(result)
