from math import prod

with open("input") as f:
    input = [line.strip() for line in f.readlines()]


workflows = {}
for line in input:
    if not line:
        break
    name, rest = line.split("{")
    workflows[name] = [
        (
            {
                cond[0][0]: (1, int(cond[0][2:]) - 1)
                if cond[0][1] == "<"
                else (int(cond[0][2:]) + 1, 4000)
            },
            then,
        )
        if cond
        else ({}, then)
        for *cond, then in (check.split(":") for check in rest[:-1].split(","))
    ]


accepted = []

start = {c: (1, 4000) for c in "xmas"}
q = [(start, "in")]
while q:
    state, workflow = q.pop()
    if workflow == "A":
        accepted.append(state)
        continue
    if workflow == "R":
        continue
    for cond, then in workflows[workflow]:
        modstate = state.copy()
        for cat, (lo, hi) in cond.items():
            slo, shi = state[cat]
            modstate[cat] = (max(lo, slo), min(hi, shi))
            state[cat] = (hi + 1, shi) if lo == 1 else (slo, lo - 1)
        q.append((modstate, then))


result = sum(prod(hi - lo + 1 for lo, hi in state.values()) for state in accepted)
print(result)
