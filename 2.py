f = open("2.txt")
l = f.readlines()
ct = 0

def is_safe(report):
    diffs = [abs(report[i] - report[i+1]) for i in range(len(report) - 1)]
    return (all(x > 0 for x in diffs) and all(1 <= x <= 3 for x in diffs) and 
            (all(report[i] <= report[i+1] for i in range(len(report) - 1)) or 
             all(report[i] >= report[i+1] for i in range(len(report) - 1))))

def can_be_safe(report):
    n = len(report)
    for i in range(n):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports(data):
    safe_count = 0
    for report in data:
        report = list(map(int, report.split()))
        if is_safe(report) or can_be_safe(report):
            safe_count += 1
    return safe_count

print(count_safe_reports(l))  # Should output 4 for the example.

# for i in l:
#     x = list(map(int, i.split()))
#     def check(x):
#         if x[1] > x[0]:
#             if x[1] - x[0] <= 3 and x[1] - x[0] > 0:
#                 if forward(x) == 1:
#                     return 1
#             t = x
#             for i in x:
#                 t.remove(i)
#                 if forward(x) == 1:
#                     return 1
#         else:
#             if x[0] - x[1] <= 3 and x[0] - x[1] > 0:
#                 if back(x) == 1:
#                     return 1

#             t = x
#             for i in x:
#                 t.remove(i)
#                 if forward(x) == 1:
#                     return 1

#     def forward(x):
#         for s in range(1, len(x)):
#             dif = x[s] - x[s-1]
#             if dif > 0 and dif <= 3:
#                 continue
#             else:
#                 br = True
#                 break
#         else:
#             return 1
#         return 0
#     def back(x):
#         for s in range(1, len(x)):
#             dif =  x[s-1] -x[s] 
#             if dif > 0 and dif <= 3:
#                 continue
#             else:
#                 break
#         else:
#             return 1
#         return 0
#     d = check(x)
#     if d == 1:
#         ct+=1
# print(ct)      
