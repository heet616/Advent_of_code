import time
from concurrent.futures import ThreadPoolExecutor

def parse_file():
    vals = {}
    gates = {}
    with open(f"{__file__.split('.')[0]}.txt") as f:
        while True:
            l = f.readline().strip()
            if l == "":
                break
            l = l.split(":")
            vals[l[0]] = int(l[1])
        while True:
            l = f.readline().strip().split(" ")
            if len(l) <= 1:
                break
            if l[0] not in gates:
                gates[l[0]] = {l[2]: [l[1], l[-1]]}
            else:
                gates[l[0]][l[2]] =[l[1], l[-1]]
            if l[2] not in gates:
                gates[l[2]] = {l[0]: [l[1], l[-1]]}
            else:
                gates[l[2]][l[0]] =[l[1], l[-1]]

    
    return vals, gates

vals, gates = parse_file()
print(gates)
def calc(i, j):
    c = gates[i][j]
    if c[0] == "AND":
        vals[c[1]] = vals[i] & vals[j]
    elif c[0] == "OR":
        vals[c[1]] = vals[i] | vals[j]
    else:
        vals[c[1]] = vals[i] ^ vals[j]

def func():
    while gates:
        found = set()
        for i in vals:
            if i in gates:
                print(i, gates[i])
                print(vals)
                for j in gates[i]:
                    if j in vals and (j, i) not in found:
                        found.add((i,j))
        # if len(found) == 0:
            # break
        for i,j in found:
            calc(i, j)
            gates[i].pop(j)
            if len(gates[i]) == 0:
                gates.pop(i)
            if j in gates:
                gates[j].pop(i)
                if len(gates[j]) == 0:
                    gates.pop(j)


z = {}
func()
for i in vals:
    if i[0] == "z":
        z[int(i[1:])] = vals[i]
print(z)
ans = "".join(str(z[i]) for i in sorted(z.keys(), reverse=True))
print(ans)
