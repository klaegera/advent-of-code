with open("input") as f:
    input = [line.strip() for line in f.readlines()]

A = int(input[0].split()[-1])
B = int(input[1].split()[-1])
C = int(input[2].split()[-1])
text = [int(x) for x in input[4].split()[1].split(",")]

combo = lambda op: [0, 1, 2, 3, A, B, C][op]

ip = 0
out = []
while ip < len(text):
    inst, oper = text[ip : ip + 2]
    match inst:
        case 0:
            A = A // 2 ** combo(oper)
        case 1:
            B = B ^ oper
        case 2:
            B = combo(oper) % 8
        case 3:
            if A:
                ip = oper
                ip -= 2
        case 4:
            B ^= C
        case 5:
            out += [str(combo(oper) % 8)]
        case 6:
            B = A // 2 ** combo(oper)
        case 7:
            C = A // 2 ** combo(oper)
    ip += 2

print(",".join(out))
