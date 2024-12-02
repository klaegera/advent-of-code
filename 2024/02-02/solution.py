with open("input") as f:
    input = f.readlines()


def safe(report):
    diff = [a - b for a, b in zip(report, report[1:])]
    return all(0 < abs(d) < 4 for d in diff) and sum(d > 0 for d in diff) in (
        0,
        len(diff),
    )


def safe_tolerant(report):
    if safe(report):
        return True
    for i in range(len(report)):
        if safe(report[:i] + report[i + 1 :]):
            return True
    return False


result = sum(safe_tolerant([int(n) for n in line.split()]) for line in input)

print(result)
