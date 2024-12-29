with open("input") as f:
    input = [line.strip() for line in f.readlines()]

files = []
spaces = []
block = 0
for i, c in enumerate(input[0]):
    size = int(c)
    if i % 2:
        spaces.append([block, size])
    else:
        files.append([block, i // 2, size])
    block += size

for file in reversed(files):
    file_block, _, file_size = file
    for space in spaces:
        space_block, space_size = space
        if space_block > file_block:
            break
        if space_size >= file_size:
            file[0] = space_block
            space[0] += file_size
            space[1] -= file_size
            break

result = sum(id * (block + block + size - 1) * size // 2 for block, id, size in files)

print(result)
