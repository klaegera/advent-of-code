with open("input") as f:
    input = [line.strip() for line in f.readlines()]


graph = [[[] for _ in range(len(input[0]) + 1)] for _ in range(len(input) + 1)]

for r, row in enumerate(input):
    for c, pipe in enumerate(row):
        node = graph[r][c]
        if pipe == "S":
            prev = start = node
            curr = graph[r + 1][c]  # set manually
        if pipe in "|7F":
            node.append(graph[r + 1][c])
        if pipe in "7J-":
            node.append(graph[r][c - 1])
        if pipe in "|JL":
            node.append(graph[r - 1][c])
        if pipe in "-FL":
            node.append(graph[r][c + 1])


result = 1
while curr is not start:
    result += 1
    prev, curr = curr, curr[0] if curr[0] is not prev else curr[1]

print(result // 2)
