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

c = correlate2d(a, k, "same")
result = ((10 <= c) & (c <= 13)).sum()

print(result)
