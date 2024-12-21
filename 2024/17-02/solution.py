with open("input") as f:
    input = [line.strip() for line in f.readlines()]

text = [int(x) for x in input[4].split()[1].split(",")]


def rec(i=1, A=0):
    if i > len(text):
        return A
    A <<= 3
    for b in range(8):
        A2 = A + b
        if (A2 ^ (A2 >> (~b % 8))) % 8 == text[-i]:
            if x := rec(i + 1, A2):
                return x


print(rec())
