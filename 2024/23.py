import time
from concurrent.futures import ThreadPoolExecutor

def parse_file():
    connections = {}

    with open(f"{__file__.split('.')[0]}.txt") as f:
        while True:
            l = f.readline().strip()
            if l == "":
                break
            l = l.split("-")
            if l[0] in connections:
                connections[l[0]].append(l[1])
            else:
                connections[l[0]] = [l[1]]
            if l[1] in connections:
                connections[l[1]].append(l[0])
            else:
                connections[l[1]] = [l[0]]
    
    return connections

connections = parse_file()

visited = set()
cycles = []
def visit(u, parents, c, parent):
    if c[u] == 2:
        return
    if c[u] == 1:
        cycle = [u]
        cur = parent
        while cur != u:
            cur = parent
            cycle.append(cur)
        cycles.append(cycle)
    c[u] = 1
    for j in connections[u]:
        p[j] = u
        visit(j, parents, c, u)

    c[u] = 2
    visited.add(u)

for i in connections:
    
    visit(i, parents, colors, None)
