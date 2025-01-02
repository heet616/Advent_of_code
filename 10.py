def parse_file():
    grid = []
    with open(f"{__file__.split('.')[0]}.txt") as f:
        for l in f:
            grid.append(list(map(int, list(l.strip()))))
    return grid

grid = parse_file()

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

m = len(grid)
n = len(grid[0])

def isvalid(x,y):
    return x < m and y < n and x >= 0 and y >= 0

def find(grid, i, j, m, n, se):
    num = grid[i][j]
    if num == 9:
        se.add((i,j))
        return 1
    ans = 0
    for di, dj in directions:
        if isvalid(i+di, j+dj) and grid[i+di][j+dj] == num + 1:
            ans += find(grid, i + di, j+dj, m, n, se)
    return ans
trails = 0
scores = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            se = set()
            trails += find(grid, i, j, m, n, se)
            scores += len(se)
print(scores)
print(trails)

# print(solve_1())
# print(solve_2())
