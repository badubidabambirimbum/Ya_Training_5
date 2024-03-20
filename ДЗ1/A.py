with open("input.txt", "r") as input:
    P,V = list(map(int, input.readline().split()))
    Q,M = list(map(int, input.readline().split()))

mx1 = P+V
mn1 = P-V

mx2 = Q+M
mn2 = Q-M

if mx1 < mn2:
    print((mx1 - mn1 + 1) + (mx2 - mn2 + 1))
elif mx2 < mn1:
    print((mx1 - mn1 + 1) + (mx2 - mn2 + 1))
elif mx1 >= mn2:
    print(max(mx1,mx2) - min(mn1,mn2) + 1)
elif mx2 >= mn1:
    print(max(mx1,mx2) - min(mn1,mn2) + 1)