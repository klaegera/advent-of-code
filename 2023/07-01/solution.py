from collections import Counter

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

hands = [line.split() for line in input]

rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

sortable = []
for hand, bid in hands:
    hist = sorted(Counter(hand).values())
    if hist[-1] == 5:
        type = 6
    elif hist[-1] == 4:
        type = 5
    elif hist[-1] == 3 and hist[-2] == 2:
        type = 4
    elif hist[-1] == 3:
        type = 3
    elif hist[-1] == 2 and hist[-2] == 2:
        type = 2
    elif hist[-1] == 2:
        type = 1
    else:
        type = 0

    sortable.append([type, [rank.index(c) for c in hand], int(bid)])

result = sum((i + 1) * bid for i, (_, _, bid) in enumerate(sorted(sortable)))

print(result)
