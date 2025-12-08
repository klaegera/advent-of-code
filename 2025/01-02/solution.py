with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
s = 50
for line in lines:
    dir, n = line[0], int(line[1:])
    d, n = divmod(n, 100)
    result += d
    if dir == "R":
        d, s = divmod(s + n, 100)
        result += d
    else:
        result += s != 0 and n >= s
        s = (s - n) % 100

print(result)
