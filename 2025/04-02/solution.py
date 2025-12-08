import numpy as np
from scipy.signal import correlate2d

with open("input") as f:
    inp = [list(line.strip()) for line in f.readlines()]

a = (np.array(inp) == "@") * 1

k = np.array(
    [
        [1, 1, 1],
        [1, 10, 1],
        [1, 1, 1],
    ]
)

result = 0
while True:
    c = correlate2d(a, k, "same")
    removable = (10 <= c) & (c <= 13)
    num = removable.sum()
    if num == 0:
        break
    result += num
    a -= removable

print(result)
