import pygame as py
import time
def parse_file():
    robots = []
    with open(f"{__file__.split('.')[0]}.txt") as f:
        while True:
            l = f.readline()
            if l == "":
                break
            l = l.strip().split(' ')
            p = l[0][2:].split(",")
            v = l[1][2:].split(",")
            robots.append([int(p[0]), int(p[-1]), int(v[0]), int(v[-1])])
    return robots

robots = parse_file()
sum_ = 0
height = 103
width = 101
test_h = 7
test_w = 11

def solve_1():
    positions = {}

    for p_x, p_y, v_x, v_y in robots:
        pos = (p_x, p_y)
        if pos in positions:
            positions[pos] += 1
        else:
            positions[pos] = 1
    n_robots = len(robots)
    for _ in range(100):
        i = 0
        for p_x, p_y, v_x, v_y in robots:
            x = p_x
            y = p_y
            p_x = (p_x + v_x)%width
            p_y = (p_y + v_y)%height
            pos = (p_x, p_y)
            positions[(x,y)] -= 1
            if pos in positions:
                positions[pos] += 1
            else:
                positions[pos] = 1
            robots[i][0] = p_x
            robots[i][1] = p_y
            i+=1

    quad = [0, 0, 0, 0]
    q_x = width//2
    q_y = height//2

    for pos in positions:

        if pos[0] == q_x or pos[1] == q_y:
            continue
        if pos[0] < q_x:
            if pos[1] < q_y:
                quad[0]+=positions[pos]
            else:
                quad[1]+=positions[pos]
        else:
            if pos[1] < q_y:
                quad[2]+=positions[pos]
            else:
                quad[3]+=positions[pos]

    print(quad[0] * quad[1]*quad[2]*quad[3])

def clear(canvas):
    canvas.fill((0, 0, 0))
    py.display.flip()

def update_screen(positions, canvas, frame):
    for i, j, _, _ in positions:
        py.draw.rect(canvas, (124, 252, 0), (i * 10, j * 10, 10, 10))  
    py.display.flip()
    py.image.save(canvas, f"{frame}.jpeg")

def solve_2():
    py.init()
    canvas = py.display.set_mode((width*10, height*10))
    positions = {}

    for p_x, p_y, v_x, v_y in robots:
        pos = (p_x, p_y)
        if pos in positions:
            positions[pos] += 1
        else:
            positions[pos] = 1
    n_robots = len(robots)
    for frame in range(10000):
        i = 0
        for p_x, p_y, v_x, v_y in robots:
            x = p_x
            y = p_y
            p_x = (p_x + v_x)%width
            p_y = (p_y + v_y)%height
            pos = (p_x, p_y)
            positions[(x,y)] -= 1
            if pos in positions:
                positions[pos] += 1
            else:
                positions[pos] = 1
            robots[i][0] = p_x
            robots[i][1] = p_y
            i+=1
        clear(canvas)
        update_screen(robots, canvas, frame)
        print(frame)



solve_2()

