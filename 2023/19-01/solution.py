with open("input") as f:
    input = [line.strip() for line in f.readlines()]

# with eval for the lols

accepted = 0


def accept(part):
    global accepted
    accepted += sum(part.values())


workflows = {"A": "accept(part)", "R": "", "accept": accept}
parts = None
for line in input:
    if not line:
        parts = []
        continue
    if parts is None:
        name, rest = line.split("{")
        workflows[name] = "".join(
            f"{then} if {cond[0]} else " if cond else then
            for *cond, then in (check.split(":") for check in rest[:-1].split(","))
        )
    else:
        parts.append(
            dict(zip("xmas", (int(cat.split("=")[1]) for cat in line[1:-1].split(","))))
        )


for part in parts:
    expr = workflows["in"]
    while expr:
        expr = eval(expr, workflows, {"part": part} | part)

print(accepted)
