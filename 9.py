file_seq = []
def parse_file():
    with open(f"{__file__.split('.')[0]}.txt") as f:
        for l in f:
            file_seq.extend(list(l.strip()))

parse_file()

def parse_1(disk_sequence):
    m = len(file_seq)
    id_ = 0
    for i in range(0, m, 2):
        disk_sequence.extend([id_]*int(file_seq[i]))
        id_ += 1
        if i+1 < m:
            disk_sequence.extend(['.']*(int(file_seq[i+1])))
    return disk_sequence

def solve_1():
    i = 0
    disk_sequence = []
    parse_1(disk_sequence)
    l = len(disk_sequence)
    j = l - 1
    while i < j:
        if disk_sequence[i] == ".":
            while disk_sequence[j] == ".":
                j-=1
            disk_sequence[i] = disk_sequence[j]
            disk_sequence[j] = "."
        i+=1

    sum_ = sum(i*j for i, j in enumerate(disk_sequence) if j!= ".")
    return sum_

def parse_2(disk_sequence):
    m = len(file_seq)
    id_ = 0
    for i in range(0, m, 2):
        disk_sequence.append([id_]*int(file_seq[i]))
        id_ += 1
        if i+1 < m:
            disk_sequence.append(['.']*(int(file_seq[i+1])))
    return disk_sequence

def solve_2():
    disk_sequence = []
    parse_2(disk_sequence)
    l = len(disk_sequence)
    i = l - 1
    while i >= 0:
        if "." in disk_sequence[i]:
            i-=1
            continue
        file_mem = disk_sequence[i]
        m = len(file_mem)
        j = 0
        while j <  l and ("." not in disk_sequence[j] or len(disk_sequence[j]) < m):
            j+=1
        if j > i:
            i-=1
            continue
        co = disk_sequence[j]
        if len(co) != m:
            disk_sequence.insert(j+1, ["."]*(len(co) - m))
            i+=1
        co = file_mem[:]
        for ind, x in enumerate(file_mem):
            file_mem[ind] = "."
        disk_sequence[i] = file_mem
        disk_sequence[j] = co
        i-=1
    final = []
    for i in disk_sequence:
        final.extend(i)
    sum_ = sum(i*j for i, j in enumerate(final) if j != ".")
    return sum_

print(solve_1())
print(solve_2())
