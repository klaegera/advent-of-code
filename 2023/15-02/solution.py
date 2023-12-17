with open("input") as f:
    input = [line.strip() for line in f.readlines()]

steps = input[0].split(",")


boxes = [{} for _ in range(256)]
for step in steps:
    if "-" in step:
        label, focus = step[:-1], None
    else:
        label, focus = step[:-2], step[-1]

    hash = 0
    for c in label:
        hash += ord(c)
        hash *= 17
        hash %= 256

    if focus:
        boxes[hash][label] = focus
    else:
        boxes[hash].pop(label, None)

result = 0
for b, box in enumerate(boxes):
    for l, lens in enumerate(box.values()):
        result += (b + 1) * (l + 1) * int(lens)

print(result)
