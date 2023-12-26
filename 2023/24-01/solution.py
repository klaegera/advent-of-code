import numpy as np

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

hail = [
    (np.c_[[x, y]], np.c_[[vx, vy]])
    for x, y, _, vx, vy, _ in (
        map(int, line.replace(" @ ", ", ").split(", ")) for line in input
    )
]

result = 0
for i, (a, va) in enumerate(hail):
    for b, vb in hail[i + 1 :]:
        try:
            t = np.linalg.solve(np.hstack((va, -vb)), b - a)
            if (t >= 0).all():
                x = a + t[0] * va
                if (200000000000000 <= x).all() and (x <= 400000000000000).all():
                    result += 1
        except:
            pass

print(result)
