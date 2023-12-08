import math

with open("input") as f:
    input = f.readlines()

directions = input[0].strip()
graph = {line[:3]: (line[7:10], line[12:15]) for line in input[2:]}

result = []

# only works due to the special properties of the input:
# perfect cycles (end node restarts the cycle),
# single target node (**Z) on cycle,
# target node is end node,
# cycle lengths divisible by number of directions
nodes = [node for node in graph if node[-1] == "A"]
for node in nodes:
    steps = 0
    while node[-1] != "Z":
        node = graph[node][directions[steps % len(directions)] == "R"]
        steps += 1
    result.append(steps)

print(math.lcm(*result))

# Analysis:

# for node in nodes:
#     visited = set()
#     curr = node
#     steps = 0
#     while True:
#         curr = graph[curr][directions[steps % len(directions)] == "R"]
#         state = curr, steps % len(directions)
#         if state in visited and steps > 100000:
#             break
#         visited.add(state)
#         steps += 1
#         if curr[-1] == "Z":
#             print(node, state, steps)
#     print(node, state, steps)
