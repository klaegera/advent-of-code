with open("input") as f:
    input = [line.strip() for line in f.readlines()]

springs = [(s, tuple(int(n) for n in nums.split(","))) for s, nums in (line.split() for line in input)]


def dp(spring, num, started=False):
    if not "#" in spring and not any(num):
        return 1
    if not spring or not num:
        return 0
    match spring[0]:
        case ".":
            if num[0] == 0:
                return dp(spring[1:], num[1:])
            elif started:
                return 0
            else:
                return dp(spring[1:], num)
        case "#":
            if num[0] == 0:
                return 0
            else:
                return dp(spring[1:], (num[0] - 1,) + num[1:], True)
        case "?":
            return dp("#" + spring[1:], num, started) + dp("." + spring[1:], num, started)

result = sum(dp(*input) for input in springs)

print(result)
