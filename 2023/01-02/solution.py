import re

with open("input") as f:
    input = f.readlines()

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

result = 0

regex = re.compile(f"(?=({"|".join(digits.keys())}|[0-9]))")
for line in input:
    first = None
    for match in re.finditer(regex, line):
        if first is None:
            first = match.group(1)
    last = match.group(1)

    first, last = (digits[x] if x in digits else x for x in (first, last))
    result += int(first + last)

print(result)
