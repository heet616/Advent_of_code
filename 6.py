
def parse(i):
    if i == ".":
        return 0
    if i == "^":
        return 2
    if i == "#":
        return -1

def find(d, pos, xy_set, n, m, xyd):
    y, x = pos
    if d == 0:
        while y >= 0 and grid[y][x] != -1:
            if (y, x, d) in xyd:
                return False
            xyd.add((y,x,d))
            xy_set.add((y,x))
            y -= 1
        if y >= 0 and  grid[y][x] == -1:
            y+=1
    elif d == 1:
        while x < n and grid[y][x] != -1:
            if (y, x, d) in xyd:
                return False
            xyd.add((y,x,d))
            xy_set.add((y,x))
            x += 1
        if x < n and grid[y][x] == -1:
            x-=1
    elif d == 2:
        while y < m and grid[y][x] != -1:
            if (y, x, d) in xyd:
                return False
            xyd.add((y,x,d))
            xy_set.add((y,x))
            y+=1
        if y < m and grid[y][x] == -1:
            y-=1
    else:
        while x >= 0 and grid[y][x] != -1:
            if (y, x, d) in xyd:
                return False
            xyd.add((y,x,d))
            xy_set.add((y,x))
            x -= 1
        if x >= 0 and  grid[y][x] == -1:
            x+=1

    pos[0] = y
    pos[1] = x
    return True

orig_set = set()
grid = []

def travel(pos, xyd, xy_set):
    d = 0
    count = 0
    while pos[1] >= 0 and pos[1] < n and pos[0] >= 0 and pos[0] < m:
        flag = find(d, pos, xy_set, n, m, xyd)
        if not flag:
            return 1
        d = (d+1)%4
    # print(len(xy_set))
    return 0

def solve_2(pos, xy_set):
    obs_c = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = -1
                obs_c += travel(pos[:], set(), set())
                grid[i][j] = 0
    print(obs_c)

pos = [-1, -1]
with open(f"{__file__.split('.')[0]}.txt") as f:
    i = 0
    for line in f:
        line = line.strip()
        grid.append(list(map(lambda x: parse(x), line)))
        if 2 in grid[-1]:
            pos[1] = grid[-1].index(2)
            pos[0] = i
        i += 1

m = len(grid)
n = len(grid[0])
xy_set = set()
travel(pos[:], set(), xy_set)
solve_2(pos[:], xy_set)
