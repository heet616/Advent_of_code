lines = []

with open(f"{__file__.split('.')[0]}.txt") as f:
    lines = f.readlines()

rules = []
updates = []

before = {}
after = {}
valid_upt = []

def parse_rules(rules):
    for l in rules:
        l = l.split("|")
        if l[1] not in before:
            before[l[1]] = [l[0]]
        else:
            before[l[1]].append(l[0])
        if l[0] not in after:
            after[l[0]] = [l[1]]
        else:
            after[l[0]].append(l[1])

def is_valid(l):
    le = len(l)
    for i in range(le):
        be = l[:i]
        af = l[i+1:]
        for j in be:
            if j in after[l[i]]:
                return False
        for j in af:
            if j in before[l[i]]:
                return False
    return True

def solve_1():
    mid = 0
    parse_rules(rules)
    for l in updates:
        l = l.split(",")
        le = len(l)
        if is_valid(l):
            mid += int(l[le//2])
            valid_upt.append(l)
    return mid

def solve_2():
    mid = 0
    parse_rules(rules)
    for l in updates:
        l = l.split(",")
        le = len(l)
        new_l = l[:]
        if is_valid(l):
            continue
        new_l = []
        for i in l:
            ind = 0
            for j in new_l:
                if j in after[i]:
                    break
                ind +=1
            new_l.insert(ind, i)
        mid+= int(new_l[le//2])  
    return mid      

for line in lines:
    l = line.strip()
    if l == "":
        continue
    if "|" in l:
        rules.append(l)
    else:
        updates.append(l)

print(solve_1())
print(solve_2())
