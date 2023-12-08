with open("input") as f:
    input = f.readlines()

directions = input[0].strip()
graph = {line[:3]: (line[7:10], line[12:15]) for line in input[2:]}

result = 0

node = "AAA"
while node != "ZZZ":
    node = graph[node][directions[result % len(directions)] == "R"]
    result += 1

print(result)
