with open("input") as f:
    input = f.readlines()

result = sum(
    input[r][c] == "A"
    and (input[r - 1][c - 1], input[r + 1][c + 1]) in (("M", "S"), ("S", "M"))
    and (input[r - 1][c + 1], input[r + 1][c - 1]) in (("M", "S"), ("S", "M"))
    for r in range(1, len(input) - 1)
    for c in range(1, len(input[0]) - 1)
)

print(result)
