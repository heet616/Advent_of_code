lines = []
def parse():
    with open(f"{__file__.split('.')[0]}.txt") as f:
        for l in f:
            l = l.replace("#", '.')
            lines.append(l.strip())

parse()
di = {}
m = len(lines)
n = len(lines[0])
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch != ".":
            if ch in di:
                di[ch].append((j, i))
            else:
                di[ch] = [(j,i)]
pts = set()
for freq in di:
    cords = di[freq]
    l = len(cords)
    for co in range(l):
        for co2 in range(co+ 1, l):
            x = cords[co2][0] - cords[co][0]
            y = cords[co2][1] - cords[co][1]
            new_x = cords[co][0]
            new_y = cords[co][1] 
            while new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                pts.add((new_x, new_y))
                new_x -= x
                new_y -= y
            new_x = cords[co2][0]
            new_y = cords[co2][1]
            while new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                pts.add((new_x, new_y)) 
                new_x += x
                new_y += y

for i in pts:
    x = lines[i[1]][:i[0]] + "#" + lines[i[1]][i[0]+1:]
    lines[i[1]] =x
for i in lines:
    print(i)

print(len(pts))