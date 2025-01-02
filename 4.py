with open("4.txt") as f:
    data = f.readlines()
ans = 0
data = [i.strip() for i in data]
m = len(data) 

for i in data:
    ans += i.count("XMAS")
    ans += i.count("SAMX")

for j in range(m):
    diag = []
    for k in range(0, m):
        diag.append(data[k][j])
    st = "".join(diag)
    ans += st.count("XMAS")
    ans += st.count("SAMX")

for off in range(m-1):
    diag = []
    diag2 = []
    for i in range(m):
        if i + off >= m:
            break
        diag.append(data[i][i+off])
        if off == 0:
            continue
        diag2.append(data[i + off][i])
    st = "".join(diag)
    st2 = "".join(diag2)
    ans += st.count("XMAS")
    ans += st2.count("XMAS")
    ans += st.count("SAMX") 
    ans += st2.count("SAMX")


di = [[] for i in range(m + m - 1)] 

for i in range(m): 
    for j in range(m): 
        di[i + j].append(data[j][i])

for i in di: 
    st = "".join(i)
    ans += st.count("XMAS")
    ans += st.count("SAMX") 

print(ans)
ans = 0

for i in range(1, m-1):
    for j in range(1, m-1):
        if data[i][j] == "A":
            if data[i+1][j-1] == "S" and data[i+1][j+1] == "S" and data[i-1][j+1] == "M" and data[i-1][j-1] == "M":
                ans += 1
            elif data[i-1][j+1] == "S" and data[i+1][j+1] == "S" and data[i+1][j-1] == "M" and data[i-1][j-1] == "M":
                ans += 1
            elif data[i+1][j-1] == "S" and data[i-1][j-1] == "S" and data[i-1][j+1] == "M" and data[i+1][j+1] == "M":
                ans += 1
            elif data[i-1][j+1] == "S" and data[i-1][j-1] == "S" and data[i+1][j-1] == "M" and data[i+1][j+1] == "M":
                ans += 1
"""
X X S
X X X
S X X
"""
print(ans)
