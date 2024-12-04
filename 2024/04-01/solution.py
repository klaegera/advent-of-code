with open("input") as f:
    input = f.readlines()

result = 0
for r in range(len(input)):
    for c in range(len(input[0])):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                for step, char in enumerate("XMAS"):
                    nr, nc = r + dr * step, c + dc * step
                    if not (
                        0 <= nr < len(input)
                        and 0 <= nc < len(input[0])
                        and input[nr][nc] == char
                    ):
                        break
                else:
                    result += 1


print(result)
