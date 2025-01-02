import re
f = open("3.txt")
data = f.readline()

sum_ = 0
x = data[data.index("don't()"):]
parts = [data[:data.index("don't()")]]
print(x)
parts.extend(re.findall(r"do\(\)(.*?)(?:don't\(\)|$)", rf"{x}"))
for p in parts:
    sum_ += sum(int(m)* int(n) for m, n in re.findall(r"mul\(([\d]{1,3}),([\d]{1,3})\)", rf"{p}"))
# ind = re.findall(r"mul\(([\d]{1,3}),([\d]{1,3})\)", rf"{i}")

print(sum_)

total2 = 0
enabled = True
for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        total2 += x * enabled

print(total2)