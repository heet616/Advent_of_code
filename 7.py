equations = []
def parse():
    with open(f"{__file__.split('.')[0]}.txt") as f:
        for l in f:
            v, e = l.split(":")
            e = list(map(int, e.strip().split(" ")))
            equations.append((int(v),e))

parse()
print(equations)

operators = ["+", "*"]

def recur(ans, ind, eq):
    if ind == len(eq):
        yield ans
        return 
    yield from recur(ans + eq[ind], ind+1, eq)
    yield from recur(ans * eq[ind], ind + 1, eq)
    yield from recur(int(str(ans) + str(eq[ind])), ind + 1, eq)
count = 0
sum_ = 0
for val, eq in equations:
    s = set()
    s = (recur(eq[0], 1, eq))
    for i in s:
        if i == val:
            count+=1
            sum_ += val
            break
print(sum_)