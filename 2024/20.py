import pygame as py
def parse_file():
    grid = []
    with open(f"{__file__.split('.')[0]}.txt") as f:
        y = 0
        while True:
            line = f.readline().strip()
            if line == "":
                break
            line = list(line)
            if "S" in line:
                sy = y
                sx = line.index("S")
            y += 1
            grid.append(line)
    return grid, sx, sy

grid, x, y = parse_file()

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cheats = [((0, 1, 1, 0), (1, 0, 0, 1)), ((0, 1, -1, 0), (-1, 0, 1, 0)), ((0, -1, -1, 0), (-1, 0, 0, -1)), ((0, -1, 1, 0), (1, 0, 0, -1)), (1, 0, 1, 0), (-1, 0, -1, 0), (0, 1, 0, 1), (0, -1, 0, -1)]
m = len(grid[0])
n = len(grid)
def isvalid(y,x):
    return x < m and y < n and x >= 0 and y >= 0

visited = {}
cheat_points = {}
step = 0
points = set((".", "E"))
while grid[y][x] != "E":
    f_cords = None
    for dy, dx in directions:
        ty = y + dy
        tx = x + dx
        if not isvalid(ty, tx):
            continue
        if grid[ty][tx] in points and (ty, tx) not in visited:
            visited[(ty, tx)] = step 
            f_cords = (ty, tx)
            break
    for dir in cheats:
        flag = True
        if len(dir) == 2:
            for dy1, dx1, dy2, dx2 in dir:
                tx = x + dx1
                ty = y + dy1
                if not isvalid(ty, tx):
                    continue
                if grid[ty][tx] == ".":
                    flag = False
        else:
            dy1, dx1, dy2, dx2 = dir
            tx = x + dx1
            ty = y + dy1
            if not isvalid(ty, tx):
                continue
            if grid[ty][tx] == ".":
                continue

        if not flag:
            continue
        tx += dx2
        ty += dy2
        if not isvalid(ty, tx):
            continue
        if grid[ty][tx] in points and (ty, tx) not in visited:
            if (ty, tx) not in cheat_points:
                # cheat_points[(ty, tx)] = [(x, y, step)]
                cheat_points[(ty, tx)] = [step]
            else:
                # cheat_points[(ty, tx)].append((x, y, step))
                cheat_points[(ty, tx)].append(step)


    step += 1
    y,x = f_cords

count = 0
print(cheat_points)
for i in cheat_points:
    for j in cheat_points[i]:
        if visited[i] - j >= 100:
            count += 1

height = m
width = n
py.init()
factor = 5
canvas = py.display.set_mode((width*factor, height*factor))
font = py.font.SysFont('Arial', 5)

def update_screen(grid, canvas, cheat_points, font):
    canvas.fill((0, 0, 0))
    for i in range(height):
        for j in range(width):
            canvas.blit(font.render(grid[i][j], True, (255,0,0)), (j*factor, i*factor))
            if (i, j) in cheat_points:
                py.draw.rect(canvas, (255, 255, 255), (j * factor, i * factor, factor, factor))  
    py.display.flip()
    # py.image.save(canvas, f"{frame}.jpeg")

print(count)

while True:
    update_screen(grid, canvas, cheat_points, font)
