from sympy import symbols, solve

with open("input") as f:
    input = [line.strip() for line in f.readlines()]

a, v = list(
    zip(
        *(
            ((x, y, z), (vx, vy, vz))
            for x, y, z, vx, vy, vz in (
                map(int, line.replace(" @ ", ", ").split(", ")) for line in input
            )
        )
    )
)

s, u, t = (symbols([var + str(i) for i in range(3)]) for var in "sut")

eqs = [a[i][j] - s[j] + t[i] * (v[i][j] - u[j]) for i in range(3) for j in range(3)]

solution = solve(eqs)[0]
result = sum(solution[var] for var in s)

print(result)
