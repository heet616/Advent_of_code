from collections import defaultdict
def parse_file():
    grid = []
    with open(f"{__file__.split('.')[0]}.txt") as f:
        for l in f:
            grid = list(map(int, l.strip().split(" ")))
    return grid

def blink(stones):
    new_ = defaultdict(int)
    keys = list(stones.keys())
    for i in keys:
        j = str(i)
        if i == 0:
            new_[1] += stones[i]
        elif len(j)%2 == 0:
            new_[int(j[:len(j)//2])] += stones[i]
            new_[int(j[len(j)//2:])] += stones[i]
        else:
            new_[i*2024] += stones[i]
    return new_

vals = parse_file()
stones = defaultdict(int)
for i in vals:
    stones[i] += 1

count = 75
while count > 0:
    count -=1
    stones = blink(stones)
print(sum(stones.values()))
