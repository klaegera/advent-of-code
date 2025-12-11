with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

import numpy as np
from scipy.optimize import linprog

result = 0
for line in lines:
    _, *rest = line.split()
    *buttons, target = [[int(l) for l in r[1:-1].split(",")] for r in rest]

    A = np.zeros((len(target), len(buttons)), dtype=np.int32)
    for i, button in enumerate(buttons):
        A[button, i] = 1

    result += linprog([1] * len(buttons), A_eq=A, b_eq=target, integrality=1).fun

print(int(result))
