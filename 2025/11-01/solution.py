with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

g = {line.split(":")[0]: line.split()[1:] for line in lines}


def dfs(node):
    if node == "out":
        return 1
    return sum(dfs(adj) for adj in g[node])


print(dfs("you"))
