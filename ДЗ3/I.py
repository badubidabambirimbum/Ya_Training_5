with open("input.txt", "r") as input:
    s = [line.strip() for line in input]

database = dict()

i = 0
while i < len(s):
    if s[i].find(":") != -1:
        # Первая команда
        j = 1
        team1 = '"'
        while s[i][j] != '"':
            team1 += s[i][j]
            j += 1
        team1 += '"'
        if team1 not in database:
            database[team1] = {"goals": 0, "opens": 0, "sum": 0}
        # Вторая команда
        j += 5
        team2 = '"'
        while s[i][j] != '"':
            team2 += s[i][j]
            j += 1
        team2 += '"'
        if team2 not in database:
            database[team2] = {"goals": 0, "opens": 0, "sum": 0}
        # Кол-во голов левой команды
        j += 1
        goals_left = ""
        while s[i][j] != ":":
            goals_left += s[i][j]
            j += 1
        j += 1
        database[team1]["goals"] += int(goals_left)
        # Кол-во голов правой команды
        goals_right = ""
        while j < len(s[i]):
            goals_right += s[i][j]
            j += 1
        database[team2]["goals"] += int(goals_right)

        # Все голы матча
        start = ["name", 100, "team"]
        for k in range(i + 1, i + int(goals_left) + 1):
            player = ""
            j = 0
            while not s[k][j + 1].isdigit():
                player += s[k][j]
                j += 1
            if player not in database:
                database[player] = {"goals": [], "opens": 0, "team": team1}
            j += 1
            number = ""
            while s[k][j] != "'":
                number += s[k][j]
                j += 1
            # Проверка на открытие счета в матче
            if int(number) < start[1]:
                start[0] = player
                start[1] = int(number)
                start[2] = team1

            database[player]["goals"].append((int(number)))

        for k in range(i + int(goals_left) + 1, i + int(goals_left) + int(goals_right) + 1):
            player = ""
            j = 0
            while not s[k][j + 1].isdigit():
                player += s[k][j]
                j += 1
            if player not in database:
                database[player] = {"goals": [], "opens": 0, "team": team2}
            j += 1
            number = ""
            while s[k][j] != "'":
                number += s[k][j]
                j += 1
            # Проверка на открытие счета в матче
            if int(number) < start[1]:
                start[0] = player
                start[1] = int(number)
                start[2] = team2

            database[player]["goals"].append((int(number)))

        # Добавляем матчки в статистику команд
        database[team1]["sum"] += 1
        database[team2]["sum"] += 1

        if start[0] != "name":
            database[start[0]]["opens"] += 1
            database[start[2]]["opens"] += 1

        i += int(goals_right) + int(goals_left)

    elif s[i].find("Total goals for") != -1:
        j = 16
        name = ""
        while j < len(s[i]):
            name += s[i][j]
            j += 1
        if name in database:
            print(database[name]["goals"])
        else:
            print(0)

    elif s[i].find("Mean goals per game for") != -1:
        j = 24
        name = ""
        while j < len(s[i]):
            name += s[i][j]
            j += 1
        if name in database:
            print(database[name]["goals"] / database[name]["sum"])
        else:
            print(0)

    elif s[i].find("Total goals by") != -1:
        j = 15
        name = ""
        while j < len(s[i]):
            name += s[i][j]
            j += 1
        if name in database:
            print(len(database[name]["goals"]))
        else:
            print(0)

    elif s[i].find("Mean goals per game by") != -1:
        j = 23
        name = ""
        while j < len(s[i]):
            name += s[i][j]
            j += 1
        if name in database:
            print(len(database[name]["goals"]) / database[database[name]["team"]]["sum"])
        else:
            print(0)

    elif s[i].find("Goals on minute") != -1:
        j = 16
        number = ""
        while s[i][j].isdigit():
            number += s[i][j]
            j += 1
        j = 20 + len(number)
        name = ""
        while j < len(s[i]):
            name += s[i][j]
            j += 1
        counter = 0
        if name in database:
            for k in range(len(database[name]["goals"])):
                if database[name]["goals"][k] == int(number):
                    counter += 1
            print(counter)
        else:
            print(0)

    elif s[i].find("Goals on first") != -1:
        j = 15
        number = ""
        while s[i][j].isdigit():
            number += s[i][j]
            j += 1
        j = 27 + len(number)
        name = ""
        while j < len(s[i]):
            name += s[i][j]
            j += 1
        counter = 0
        if name in database:
            for k in range(len(database[name]["goals"])):
                if database[name]["goals"][k] <= int(number):
                    counter += 1
            print(counter)
        else:
            print(0)

    elif s[i].find("Goals on last") != -1:
        j = 14
        number = ""
        while s[i][j].isdigit():
            number += s[i][j]
            j += 1
        j = 26 + len(number)
        name = ""
        while j < len(s[i]):
            name += s[i][j]
            j += 1
        counter = 0
        if name in database:
            for k in range(len(database[name]["goals"])):
                if database[name]["goals"][k] >= 91 - int(number):
                    counter += 1
            print(counter)
        else:
            print(0)

    elif s[i].find("Score opens") != -1:
        j = 15
        name = ""
        while j < len(s[i]):
            name += s[i][j]
            j += 1
        if name in database:
            print(database[name]["opens"])
        else:
            print(0)

    i += 1