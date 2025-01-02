import pygame as py
import time
def parse_file():
    grid = []
    movements = []  
    x = -1
    y = -1
    with open(f"{__file__.split('.')[0]}.txt") as f:
        while True:
            l = f.readline()
            if l == "\n":
                break
            l = list(l.strip())
            
            grid.append(get_row_2(l, grid))
        while True:
            l = f.readline()
            if l == "":
                break
            l = l.strip()
            movements.extend(list(l))
    return grid, movements, x, y


def get_row_1(l, grid):
    row = []
    for i in l:
        if i == "@":
            y = len(row)
            x = len(grid)
        row.append(i)
    return row

def get_row_2(l, grid):
    row = []
    for i in l:
        if i == "O":
            row.append("[")
            row.append("]")
        elif i == "@":
            y = len(row)
            x = len(grid)
            row.append(i)
            row.append(".")
        else:
            row.append(i)
            row.append(i)
    return row


BOUNDARY = "#"
BLANK = "."
movements = {"<": (0, -1), ">": (0, 1), "^":(-1, 0), "v":(1,0)}
OBJECT = "O"
CHARACTER = "@"
grid, commands, x, y = parse_file()
sum_ = 0
height = len(grid)
width = len(grid[0])

def clear(canvas):
    canvas.fill((0, 0, 0))
    py.display.update()

def update_screen(grid, canvas, font):
    for i in range(height):
        for j in range(width):
            if grid[i][j] == BLANK:
            # py.draw.rect(canvas, (124, 252, 0), (i * 100, j * 100, 10, 100))
                # py.draw.rect(canvas, (255,159,0), (i * 10, j * 10, 10, 10))
                canvas.blit(font.render(grid[i][j], True, (255,159,122)), (i*10, j*10))
            elif grid[i][j] == BOUNDARY:
                # py.draw.rect(canvas, (0, 0, 0), (i * 10, j * 10, 10, 10))
                canvas.blit(font.render(grid[i][j], True, (0,0,0)), (i*10, j*10))
            elif grid[i][j] == CHARACTER:
                py.draw.rect(canvas, (161, 239, 139), (i * 10, j * 10, 10, 10))
            else:
                # py.draw.rect(canvas, (255, 255, 255), (i * 10, j * 10, 10, 10))
                py.draw.rect(canvas, (255,159,0), (i * 10, j * 10, 10, 10))
                # canvas.blit(font.render(grid[i][j], True, (255,159,0)), (i*10, j*10))

    py.display.update()
    time.sleep(1)

def solve_1(x, y):
    py.init()
    canvas = py.display.set_mode((width*10, height*10))
    font = py.font.SysFont('Arial', 25)
    positions = {}
    clear(canvas)
    update_screen(grid, canvas, font)
    for i in commands:
        dx, dy = movements[i]
        nx = x + dx
        ny = y + dy
        if grid[nx][ny] == BOUNDARY:
            pass
        elif grid[nx][ny] == BLANK:
            grid[x][y] = BLANK
            y = ny
            x = nx
            grid[x][y] = CHARACTER
        else:
            while grid[nx][ny] != BOUNDARY and grid[nx][ny] != BLANK:
                nx += dx
                ny += dy
            if grid[nx][ny] == BOUNDARY:
                continue
            else:
                grid[nx][ny] = OBJECT
                grid[x][y] = BLANK
                x += dx
                y += dy
                grid[x][y] = CHARACTER

        clear(canvas)
        update_screen(grid, canvas, font)

    sum_ = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == OBJECT:
                sum_ += (i)*100 + j 
    for i in grid:
        print(*i)
    print(sum_)

OBJECT_S = "["
OBJECT_E = "]"

def solve_2(x,y):
    py.init()
    canvas = py.display.set_mode((width*10, height*10))
    font = py.font.SysFont('Arial', 25)
    positions = {}
    clear(canvas)
    update_screen(grid, canvas, font)
    for i in commands:
        dx, dy = movements[i]
        nx = x + dx
        ny = y + dy
        if grid[nx][ny] == BOUNDARY:
            pass
        elif grid[nx][ny] == BLANK:
            grid[x][y] = BLANK
            y = ny
            x = nx
            grid[x][y] = CHARACTER
        else:
            while grid[nx][ny] != BOUNDARY and grid[nx][ny] != BLANK:
                if grid[nx][ny] == OBJECT_S:
                    grid
                nx += dx
                ny += dy
            if grid[nx][ny] == BOUNDARY:
                continue
            else:
                grid[nx][ny] = OBJECT
                grid[x][y] = BLANK
                x += dx
                y += dy
                grid[x][y] = CHARACTER

for i in grid:
    print(*i)
solve_2(x,y)
