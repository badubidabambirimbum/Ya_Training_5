with open("input.txt", "r") as input:
    L,x1,v1,x2,v2 = list(map(int, input.readline().split()))

if x1 == x2 or x1 + x2 == L:
    print("YES")
    print(0)

elif v1 == 0 and v2 == 0:
    print("NO")

elif v1 == 0 and v2 > 0:
    print("YES")
    if x1 > x2:
        if L - x1 - x2 > 0:
            print(min(((x1 - x2) / v2),((L - x1 - x2) / v2)))
        else:
            print((x1 - x2) / v2)
    else:
        if L - x1 - x2 > 0:
            print(min(((L + x1 - x2) / v2),((L - x1 - x2) / v2)))
        else:
            print((L + x1 - x2) / v2)

elif v1 == 0 and v2 < 0:
    print("YES")
    if x1 > x2:
        if x1 + x2 - L > 0:
            print(min(((L + x2 - x1) / -v2),((x1 + x2 - L) / -v2)))
        else:
            print((L + x2 - x1) / v2)
    else:
        if x1 + x2 - L > 0:
            print(min(((x2 - x1) / -v2),((x1 + x2 - L) / -v2)))
        else:
            print((x2 - x1) / -v2)

elif v1 > 0 and v2 == 0:
    print("YES")
    if x2 > x1:
        if L - x2 - x1 > 0:
            print(min(((x2 - x1) / v1),((L - x2 - x1) / v1)))
        else:
            print((x2 - x1) / v1)
    else:
        if L - x2 - x1 > 0:
            print(min(((L + x2 - x1) / v1),((L - x2 - x1) / v1)))
        else:
            print((L + x2 - x1) / v1)

elif v1 < 0 and v2 == 0:
    print("YES")
    if x2 > x1:
        if x2 + x1 - L > 0:
            print(min(((L + x1 - x2) / -v1),((x2 + x1 - L) / -v1)))
        else:
            print((L + x1 - x2) / -v1)
    else:
        if x2 + x1 - L > 0:
            print(min(((x1 - x2) / -v1),((x2 + x1 - L) / -v1)))
        else:
            print((x1 - x2) / -v1)

elif v1 == v2:
    print("YES")
    if v1 > 0:
        if L-(x1+x2) > 0:
            print(min((L-(x1+x2))/(v1+v2), (2*L-(x1+x2))/(v1+v2)))
        else:
            print((2*L-(x1+x2))/(v1+v2))
    else:
        print((abs(x2+x1))/abs(v2+v1))

elif v1 > 0 and v2 > 0:
    print("YES")
    if x1 > x2 and v1 > v2 or x1 < x2 and v1 < v2:
        if L - x1 - x2 > 0:
            print(min((L-(x1+x2))/(v1+v2), (2*L-(x1+x2))/(v1+v2)))
        else:
            print((2*L-(x1+x2))/(v1+v2))
    else:
        if L - x1 - x2 > 0:
            print(min(abs((x2-x1)/(v1-v2)), (L-(x1+x2))/(v1+v2), (2*L-(x1+x2))/(v1+v2)))
        else:
            print(min(abs((x2-x1)/(v1-v2)), (2*L-(x1+x2))/(v1+v2)))

elif v1 < 0 and v2 < 0:
    print("YES")
    if x1 > x2 and v1 > v2 or x1 < x2 and v1 < v2:
        print((abs(x2+x1))/abs(v2+v1))
    else:
        if L - x1 - x2 > 0:
            print(min(abs((x2-x1)/abs(v1-v2)), (L-(x1+x2))/(v1+v2), abs(2*L-(x1+x2))/abs(v1+v2)))
        else:
            print(min(abs((x2-x1)/(v1-v2)), abs(2*L-(x1+x2))/abs(v1+v2)))

elif v1 > 0 and v2 < 0:
    print("YES")
    if x1 > x2:
        if L - (x1+x2) >= 0 and abs(v1) != abs(v2):
            print(min(abs((L-x1+x2)/abs(v1-v2)),abs(L-(x1+x2))/abs(v1+v2)))
        else:
            print(abs(L-x1+x2)/abs(v1-v2))
    else:
        if L - (x1+x2) >= 0 and abs(v1) != abs(v2):
            print(min(abs((x1-x2)/abs(v1-v2)),abs(L-(x1+x2))/abs(v1+v2)))
        else:
            print(abs(x1-x2)/abs(v1-v2))

elif v1 < 0 and v2 > 0:
    print("YES")
    if x2 > x1:
        if L - (x2+x1) >= 0 and abs(v1) != abs(v2):
            print(min(abs((L-x2+x1)/abs(v2-v1)),abs(L-(x2+x1))/abs(v2+v1)))
        else:
            print(abs(L-x2+x1)/abs(v2-v1))
    else:
        if L - (x2+x1) >= 0 and abs(v1) != abs(v2):
            print(min(abs((x2-x1)/abs(v2-v1)),abs(L-(x2+x1))/abs(v2+v1)))
        else:
            print(abs(x2-x1)/abs(v2-v1))