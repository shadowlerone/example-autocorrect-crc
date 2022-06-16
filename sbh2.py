import numpy as np


def solve(case):
    terms = case.replace("+ ", "+").replace("- ", "-").split(" ")
    parsed = []
    for i in terms:
        i = i.split("^")
        if i[0].endswith("x"):
            if len(i) > 1:
                p = int(i[1])
            else:
                p = 1
            if i[0] == "x":
                c = 1
            else:
                c = int(i[0][:-1])
        else:
            c = int(i[0])
            p = 0
        if p >= 0:
            parsed.append({"coefficient": c,"power":p})
    n = parsed[0]['power']+1
    coff = np.zeros(n)
    for i in parsed:
        coff[n-i['power']-1] = i['coefficient']
    roots = np.sort(np.roots(coff).round().astype(int))
    out = ""
    for r in roots:
        if r < 0:
            op = "+"
        else:
            op = "-"
        out += f"(x{op}{abs(r)})"
    return out

if __name__ == "__main__":
	[print(solve(c)) for c in [input() for _ in range(int(input()))]]