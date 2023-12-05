with open("input") as f:
    input = f.readlines()

filtered = [[char for char in line if char.isnumeric()] for line in input]
result = sum(int(line[0] + line[-1]) for line in filtered)

print(result)
