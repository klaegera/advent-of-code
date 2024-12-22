with open("input") as f:
    input = [line.strip() for line in f.readlines()]

result = 0
for line in input:
    secret = int(line)
    for _ in range(2000):
        secret ^= secret * 64
        secret %= 16777216
        secret ^= secret // 32
        secret %= 16777216
        secret ^= secret * 2048
        secret %= 16777216
    result += secret

print(result)
