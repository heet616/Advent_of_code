import time
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

def parse_file():
    patterns = set()
    designs = set()

    with open(f"{__file__.split('.')[0]}.txt") as f:
        patterns = set(f.readline().strip().split(", "))
        f.readline()
        while True:
            l = f.readline().strip()
            if l == "":
                break
            designs.add(l)
    return patterns, designs

patterns, designs = parse_file()

ind = 0
@lru_cache(None)
def match_(start, design, l):
    if start == len(design):
        return 1
    s = 0
    for i in range(start, l):
        if design[start:i+1] in patterns:
            s += match_(i + 1, design, l)
    return s

cnt = 0
x = 0
for design in designs:
    cnt += match_(0, design, len(design))
    x  += 1
print(cnt)