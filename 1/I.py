d = {"Monday" : 52, "Tuesday" : 52, "Wednesday": 52, "Thursday" : 52, "Friday" : 52, "Saturday" : 52, "Sunday" : 52}
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
month = {"January" : 0, "February" : 31, "March": 59, "April" : 90, "May" : 120, "June" : 151, "July" : 181, "August" : 212, "September": 243, "October" : 273, "November" : 304, "December" : 334}
info = []

with open("input.txt", "r") as input:
    n = int(input.readline())
    year = int(input.readline())
    for i in range(n):
        info.append(input.readline().split())
    start = input.readline().split()[0]

d[start] += 1
week = dict()

for i in range(len(days)):
    if days[i] == start:
        p = i
        break

m = 1

for i in range(p,7):
    if m == 7:
        m = 0
    week[m] = days[i]
    m += 1
for i in range(p):
    if m == 7:
        m = 0
    week[m] = days[i]
    m += 1

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    leap_year = True
    if p < len(days) - 1:
        d[days[p+1]] += 1
    else:
        d[days[0]] += 1
else:
    leap_year = False

for i in range(len(info)):
    target = month[info[i][1]] + int(info[i][0])
    if info[i][1] != "January" and info[i][1] != "February" and leap_year == True:
        target += 1
    num = target % 7
    d[week[num]] -= 1

mx = -1
mn = 1000
res = [""] * 2
for key in d:
    if d[key] > mx:
        mx = d[key]
        res[0] = key
    if d[key] < mn:
        mn = d[key]
        res[1] = key

print(*res)