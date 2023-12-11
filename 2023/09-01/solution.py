with open("input") as f:
    input = [line.strip() for line in f.readlines()]

rows = [[int(n) for n in line.split()] for line in input]


result = 0

for row in rows:
    while any(row):
        result += row[-1]
        row = [b - a for a, b in zip(row, row[1:])]

print(result)
