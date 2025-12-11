with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

g = {line.split(":")[0]: line.split()[1:] for line in lines}

from functools import cache


@cache
def dfs(node, dest):
    if node == dest:
        return 1
    return sum(dfs(adj, dest) for adj in g.get(node, []))


print(
    dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out")
    + dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")
)
