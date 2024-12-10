with open("input") as f:
    input = [line.strip() for line in f.readlines()]

result = 0
scores = {}
for num in range(9, -1, -1):
    for r, row in enumerate(input):
        for c, val in enumerate(row):
            if val == str(num):
                if num == 9:
                    scores[(r, c)] = 1
                    continue
                score = 0
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(input) and 0 <= nc < len(input[0]):
                        if input[nr][nc] == str(num + 1):
                            score += scores[(nr, nc)]
                if num == 0:
                    result += score
                else:
                    scores[(r, c)] = score

print(result)
