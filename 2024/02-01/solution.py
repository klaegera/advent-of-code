with open("input") as f:
    input = f.readlines()


def safe(report):
    diff = [a - b for a, b in zip(report, report[1:])]
    return all(0 < abs(d) < 4 for d in diff) and sum(d > 0 for d in diff) in (
        0,
        len(diff),
    )


result = sum(safe([int(n) for n in line.split()]) for line in input)

print(result)
