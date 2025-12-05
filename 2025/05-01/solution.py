iv = []
nums = []

with open("input") as f:
    while line := f.readline().strip():
        iv.append(list(map(int, line.split("-"))))
    while line := f.readline().strip():
        nums.append(int(line))

iv.sort()

j = None
for i, (a, b) in enumerate(iv):
    if j is not None and a <= iv[j][1] + 1:
        iv[j][1] = max(iv[j][1], b)
        iv[i] = None
    else:
        j = i
iv = list(filter(None, iv))

from bisect import bisect_left

count = 0
for n in nums:
    i = bisect_left(iv, n, key=lambda v: v[1])
    if i < len(iv) and n >= iv[i][0]:
        count += 1

print(count)
