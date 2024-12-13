with open("input") as f:
    input = [line.strip() for line in f.readlines()]

result = 0

for line in input:
    shared = (set(line[: len(line) // 2]) & set(line[len(line) // 2 :])).pop()
    result += ord(shared) + (27 - ord("A") if ord(shared) < ord("a") else 1 - ord("a"))

print(result)
