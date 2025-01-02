from collections import defaultdict
def parse_file():
    claws = []
    with open(f"{__file__.split('.')[0]}.txt") as f:
        while True:
            l = f.readline().split("+")
            if len(l) == 1:
                break
            claws.append([])
            claws[-1].append((int(l[-2].split(",")[0]), int(l[-1].strip())))
            l = f.readline().split("+")
            claws[-1].append((int(l[-2].split(",")[0]), int(l[-1].strip())))
            l = f.readline().split("=")
            claws[-1].append((10000000000000 + int(l[-2].split(",")[0]), 10000000000000 + int(l[-1].strip())))
            l = f.readline()
    return claws
claws = parse_file()
sum_ = 0
for a, b, target in claws:
    a_x, a_y = a
    b_x, b_y = b
    t_x, t_y = target
    y = (a[1]*target[0] - a[0]*target[1]) /(a[1]*b[0] - b[1]*a[0])
    x = (target[0] - a[0]*y)/b[0]
    x = (target[1] - b[1]*y)/a[1]
    if x >= 0 and y >= 0 and x.is_integer() and y.is_integer():
        sum_ += x*3 + y
        print(x, y)

print(sum_)