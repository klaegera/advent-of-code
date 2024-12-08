with open("input") as f:
    input = [line.strip() for line in f.readlines()]


def calc(target, operands):
    if len(operands) == 1:
        return operands[0] == target
    a, b, *rest = operands
    return (
        calc(target, [a + b] + rest)
        or calc(target, [a * b] + rest)
        or calc(target, [int(str(a) + str(b))] + rest)
    )


result = 0
for line in input:
    target, rest = line.split(": ")
    target = int(target)
    operands = list(map(int, rest.split()))
    if calc(target, operands):
        result += target

print(result)
