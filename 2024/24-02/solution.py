with open("input") as f:
    input = [line.strip() for line in f.readlines()]

it = iter(input)
while line := next(it):
    pass

from collections import defaultdict

input_to_op = defaultdict(set)
inputs_xor = set()
inputs_and = set()
outputs = set()
num = 0

while line := next(it, None):
    a, op, b, _, c = line.split()
    input_to_op[a].add(op)
    input_to_op[b].add(op)

    if a[0] in "xy":
        i = int(a[1:])
        if i:
            num = max(num, i)
            if op == "XOR":
                inputs_xor.add(c)
            else:
                inputs_and.add(c)
    elif op == "XOR":
        outputs.add(c)

expected_outputs = {f"z{i:02}" for i in range(1, num + 1)}

result = (
    (outputs ^ expected_outputs)
    | {v for v in inputs_xor if input_to_op[v] != {"XOR", "AND"}}
    | {v for v in inputs_and if input_to_op[v] != {"OR"}}
)

print(",".join(sorted(result)))
