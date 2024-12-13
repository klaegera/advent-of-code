with open("input") as f:
    input = [line.strip() for line in f.readlines()]

result = 0
it = iter(input)
try:
    while True:
        shared = (set(next(it)) & set(next(it)) & set(next(it))).pop()
        result += ord(shared) + (
            27 - ord("A") if ord(shared) < ord("a") else 1 - ord("a")
        )
except:
    print(result)
