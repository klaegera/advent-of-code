import math
from collections import deque

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

modules = {}
for line in input:
    module, outs = line.split(" -> ")
    type, name = module[0], module[1:]
    outs = outs.split(", ")
    if "rx" in outs:
        final = name
    if type == "b":
        broadcaster = outs
    else:
        modules[name] = (type, {} if type == "&" else [False], outs)

for name, (type, state, outs) in modules.items():
    for out in outs:
        if out in modules and modules[out][0] == "&":
            modules[out][1][name] = False


cycle = {}
i = 0
while True:
    i += 1
    pulses = deque((None, out, False) for out in broadcaster)
    while pulses:
        source, dest, pulse = pulses.popleft()
        if dest in modules:
            type, state, outs = modules[dest]
            if type == "%" and not pulse:
                state[0] = not state[0]
                for out in outs:
                    pulses.append((dest, out, state[0]))
            elif type == "&":
                state[source] = pulse
                outpulse = not all(state.values())
                for out in outs:
                    pulses.append((dest, out, outpulse))
                if pulse and dest == final and source not in cycle:
                    cycle[source] = i
                    if len(cycle) == len(modules[final][1]):
                        print(math.lcm(*cycle.values()))
                        quit()
