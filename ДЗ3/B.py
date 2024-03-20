from collections import Counter

with open("input.txt", "r") as input:
    s1 = input.readline().split()[0]
    s2 = input.readline().split()[0]

def anagram(s1,s2):
    d1 = Counter(s1)
    d2 = Counter(s2)

    for key in d1:
        if key in d2 and d1[key] == d2[key]:
            continue
        else:
            return False
    return True

if anagram(s1,s2):
    print("YES")
else:
    print("NO")