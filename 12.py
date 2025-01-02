from collections import defaultdict
def parse_file():
    grid = []
    with open(f"{__file__.split('.')[0]}.txt") as f:
        for l in f:
            grid.append(list(l.strip()))
    return grid

grid = parse_file()
print(grid)

visited = set()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
m = len(grid)
n = len(grid[0])

def isvalid(x,y):
    return x < m and y < n and x >= 0 and y >= 0

def travel_region_1(i, j, visited):
    visited.add((i, j))
    perimeter = 4
    for di, dj in directions:
        n_i = di+i        
        n_j = dj+j        
        if isvalid(n_i, n_j) and grid[n_i][n_j] == grid[i][j]:
            perimeter-=1
            if (n_i, n_j) not in visited:
                perimeter += travel_region_1(n_i, n_j, visited)
    return perimeter

def travel_region_2(i, j, visited):
    visited.add((i, j))
    sides = 0  
    for di, dj in directions:
        n_i, n_j = i + di, j + dj
        if isvalid(n_i, n_j) and grid[n_i][n_j] == grid[i][j]:
            sides += 1  
            if (n_i, n_j) not in visited:
                sides += travel_region_2(n_i, n_j, visited)  # Add sides from the neighbor
    return sides


visited = set()
cost = 0
for i in range(m):
    for j in range(n):
        if (i, j) in visited:
            continue
        s = set()
        sides = travel_region_2(i, j, s)
        x = sides*len(s)
        print(sides)
        cost += x
        visited = visited.union(s)
print(cost)