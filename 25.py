import time

def parse_file():
    locks = set()
    keys = set()
    with open(f"{__file__.split('.')[0]}.txt") as f:
        while True:
            block = []
            for _ in range(7):
                block.append(list(f.readline().strip()))
            line = []
            lock = False
            for i in range(5):
                cnt = 0
                for j in range(7):
                    if block[j][i] == "#":
                        cnt += 1
                if cnt != 7 and block[0][i] == "#":
                    lock = True
                line.append(cnt-1)
            if lock:
                locks.add(tuple(line))
            else:
                keys.add(tuple(line))
            for i in block:
                print(*i)
            print(line)
            if f.readline().strip() == "END":
                break

    return locks, keys

locks, keys = parse_file()
cnt = 0
for lock in locks:
    for key in keys:
        for i in range(5):
            if lock[i] + key[i] >= 6:
                break
        else:
            cnt += 1
print(cnt)
