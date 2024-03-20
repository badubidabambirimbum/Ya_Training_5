with open("input.txt", "r") as input:
    m1 = input.readline().split()[0]
    m2 = input.readline().split()[0]
    n = int(input.readline())

team1 = int(m1[0]) + int(m2[0])
team2 = int(m1[2]) + int(m2[2])

if n == 1:
    if team1 > team2:
        print(0)
    else:
        g = team2 - team1
        if int(m2[0]) + g > int(m1[2]):
            print(g)
        else:
            print(g + 1)
else:
    if team1 > team2:
        print(0)
    else:
        g = team2 - team1
        if int(m1[0]) > int(m2[2]):
            print(g)
        else:
            print(g + 1)