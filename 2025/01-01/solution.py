with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
s = 50
for line in lines:
    dir, n = line[0], int(line[1:])
    s = (s + (1 if dir == "R" else -1) * n) % 100
    result += s == 0

print(result)
