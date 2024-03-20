with open("input.txt", "r") as input:
    w,h,c = list(map(int, input.readline().split()))
    s = input.readlines()

# data = [1,layout,width,height,dx,dy]

def database_creation(s):
    dataset = []
    i = 0
    # for i in range(len(s)):
    pic = False
    while i < len(s):
        w = s[i].split()
        if len(w) == 0:
            dataset.append([2])
        j = 0
        while j < len(w):
            if w[j][0] != "(" and pic == False:
                dataset.append([0,w[j]])
                j += 1
            else:
                if w[j][0] == "(":
                    data = [0] * 6
                    data[0] = 1
                    pic = True
                while j < len(w) and w[j][-1] != ")":
                    if w[j].find("layout=") > -1:
                        data[1] = w[j][7:]
                    elif w[j].find("width=") > -1:
                        data[2] = int(w[j][6:])
                    elif w[j].find("height=") > -1:
                        data[3] = int(w[j][7:])
                    elif w[j].find("dx=") > -1:
                        data[4] = int(w[j][3:])
                    elif w[j].find("dy=") > -1:
                        data[5] = int(w[j][3:])
                    j += 1
                if j != len(w):
                    if w[j].find("layout=") > -1:
                        data[1] = w[j][7:-1]
                    elif w[j].find("width=") > -1:
                        data[2] = int(w[j][6:-1])
                    elif w[j].find("height=") > -1:
                        data[3] = int(w[j][7:-1])
                    elif w[j].find("dx=") > -1:
                        data[4] = int(w[j][3:-1])
                    elif w[j].find("dy=") > -1:
                        data[5] = int(w[j][3:-1])
                    dataset.append(data)
                    pic = False
                    j += 1
        i += 1
    return dataset

def fragment_creation(fragment,destroy,y,H):
    y += H
    H = h
    x = 0
    fragment.clear()
    if len(destroy) == 0:
        fragment.append([0,w,0,0])
    else:
        k = 0
        while len(destroy) > 0 and k < len(destroy):
            if destroy[k][2] < y:
                destroy.remove(destroy[k])
            else:
                k += 1
        destroy.sort()
        x1 = x
        y1 = y
        for i in range(len(destroy)):
            if destroy[i][2] > y1:
                if x1 == destroy[i][0]:
                    x1 = destroy[i][1]
                elif x1 < destroy[i][0]:
                    fragment.append([x1,destroy[i][0],0,0])
                    x1 = destroy[i][1]
        if x1 != w:
            fragment.append([x1,w,0,0])

    return fragment,y,H

dataset = database_creation(s)

x = y = yx = 0
H = h
fragment = [[0,w,0,0]] # левая граница, правая граница, кол-во слов в фрагменте
destroy = [] # левая и правая граница препятствия
x2 = 0 # правый угл последнего элемента (не float) - нужен для фильтрации fragment

for i in range(len(dataset)):
    # print(fragment)
    # print(destroy)
    if dataset[i][0] == 0: # Встретили слово
        flag = False # проверка: добавили слово в файл или нет
        while flag == False:
            for j in range(len(fragment)): # Проверка фрагментов (мест, куда можно вставить что-то)
                if fragment[j][1] - fragment[j][0] > min(1,fragment[j][3]) * c + len(dataset[i][1]) * c and x2 <= fragment[j][0]:
                    fragment[j][0] = fragment[j][0] + min(1,fragment[j][3]) * c + len(dataset[i][1]) * c
                    x = fragment[j][0]
                    yx = y
                    x2 = x
                    fragment[j][2] += 1
                    fragment[j][3] += 1
                    flag = True
                    break
                elif fragment[j][1] - fragment[j][0] == min(1,fragment[j][3]) * c + len(dataset[i][1]) * c and x2 <= fragment[j][0]:
                    x = fragment[j][0] + min(1,fragment[j][3]) * c + len(dataset[i][1]) * c
                    yx = y
                    x2 = x
                    fragment.remove(fragment[j])
                    flag = True
                    break
            if flag == False: # Если не смогли вставить слово, то переходим на другую строку и формируем для нее фрагменты через destroy
                fragment, y, H = fragment_creation(fragment,destroy,y,H)
                x2 = 0


    elif dataset[i][0] == 1:
        if dataset[i][1] == 'embedded':
            flag = False # проверка: добавили слово в файл или нет
            while flag == False:
                for j in range(len(fragment)): # Проверка фрагментов (мест, куда можно вставить что-то)
                    if fragment[j][1] - fragment[j][0] > min(1,fragment[j][2]) * c + dataset[i][2] and x2 <= fragment[j][0]:
                        print(fragment[j][0]+min(1,fragment[j][2])*c,y)
                        fragment[j][0] = fragment[j][0] + min(1,fragment[j][2]) * c + dataset[i][2]
                        x = fragment[j][0]
                        yx = y
                        x2 = x
                        fragment[j][2] += 1
                        fragment[j][3] += 1
                        flag = True
                        if dataset[i][3] > H:
                            H = dataset[i][3]
                        break
                    elif fragment[j][1] - fragment[j][0] == min(1,fragment[j][2]) * c + dataset[i][2] and x2 <= fragment[j][0]:
                        print(fragment[j][0]+min(1,fragment[j][2])*c,y)
                        x = fragment[j][0] + min(1,fragment[j][2]) * c + dataset[i][2]
                        yx = y
                        x2 = x
                        fragment.remove(fragment[j])
                        flag = True
                        if dataset[i][3] > H:
                            H = dataset[i][3]
                        break
                if flag == False: # Если не смогли вставить слово, то переходим на другую строку и формируем для нее фрагменты через destroy
                    fragment, y, H = fragment_creation(fragment,destroy,y,H)
                    x2 = 0
        elif dataset[i][1] == 'surrounded':
            flag = False # проверка: добавили слово в файл или нет
            while flag == False:
                for j in range(len(fragment)): # Проверка фрагментов (мест, куда можно вставить что-то)
                    if fragment[j][1] - fragment[j][0] > dataset[i][2] and x2 <= fragment[j][0]:
                        print(fragment[j][0],y)
                        fragment[j][0] = fragment[j][0] + dataset[i][2]
                        fragment[j][2] = 0
                        fragment[j][3] = 0
                        x = fragment[j][0]
                        yx = y
                        x2 = x
                        flag = True
                        if dataset[i][3] > H:
                            destroy.append([fragment[j][0] - dataset[i][2], fragment[j][0], y + dataset[i][3]])
                        break
                    elif fragment[j][1] - fragment[j][0] == dataset[i][2] and x2 <= fragment[j][0]:
                        print(fragment[j][0],y)
                        x = fragment[j][0] + dataset[i][2]
                        x2 = x
                        yx = y
                        flag = True
                        if dataset[i][3] > H:
                            destroy.append([fragment[j][0], fragment[j][0] + dataset[i][2], y + dataset[i][3]])
                        fragment.remove(fragment[j])
                        break
                if flag == False: # Если не смогли вставить слово, то переходим на другую строку и формируем для нее фрагменты через destroy
                    fragment, y, H = fragment_creation(fragment,destroy,y,H)
                    x2 = 0
        elif dataset[i][1] == 'floating':
            x1 = x + dataset[i][4]
            y1 = yx + dataset[i][5]
            if x1 < 0:
                x = 0 + dataset[i][2]
                print(0,y1)
            elif x1 + dataset[i][2] > w:
                x = w
                print(w-dataset[i][2],y1)
            else:
                x = x1 + dataset[i][2]
                print(x1,y1)
            yx = y1
    elif dataset[i][0] == 2:
        destroy.clear()
        fragment, y, H = fragment_creation(fragment,destroy,y,H)
        x = 0
        x2 = 0
        yx = y