with open("input") as f:
    input = [line.strip() for line in f.readlines()]

steps = input[0].split(",")


result = 0
for step in steps:
    hash = 0
    for c in step:
        hash += ord(c)
        hash *= 17
        hash %= 256
    result += hash

print(result)
