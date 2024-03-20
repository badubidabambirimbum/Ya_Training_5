with open("input.txt", "r") as f:
    n, k = list(map(int, f.readline().split()))

def p2p(n, k):
    devices = dict()  # Для каждого устройства записаны его обновления в виде множества
    importance_devices = dict()  # Для каждого устройства записано то, сколько обновлений передало ему другое устройство
    updates = dict()  # Для каждого обновления указано, на скольких устройствах оно находится
    check = [0] * (n + 1)  # Проверка, что на каждом устройстве скачаны все обновления
    check[1] = 1

    for i in range(1, n + 1):
        devices[i] = set()
        importance_devices[i] = {key: 0 for key in range(1, n + 1)}
    for i in range(1, k + 1):
        devices[1].add(i)
        updates[i] = 1

    timeslot = 1
    result = [0] * (n + 1)

    while sum(check) != len(check) - 1:
        requests = []  # Запросы устройств
        download = dict()  # множество обновлений, которые надо скачать (позже добавим, у кого скачать)
        min_updates = sorted(updates.items(), key=lambda item: item[1])  # Редкость обновлений в сети

        # Составление списка обновлений, которые надо скачать, и заполнение списка запросов устройств
        for i in range(1, n + 1):
            if len(devices[i]) != k:
                for j in range(len(min_updates)):
                    if min_updates[j][0] not in devices[i]:
                        download[min_updates[j][0]] = [0, k + 1]
                        requests.append([i, i, min_updates[j][0]])
                        break

        # Ищем устройства, у которых можно запросить обновление
        for key in download:
            for i in range(1, n + 1):
                if key in devices[i] and len(devices[i]) < download[key][1]:
                    download[key] = [i, len(devices[i])]

        # Окончательно заполняем запросы. Теперь они готовы для обработки
        for i in range(len(requests)):
            requests[i][1] = download[requests[i][2]][0]

        # Упорядочиваем запросы по устройстам, у которых будет запрашивать обновление
        requests.sort(key=lambda x: x[1])

        i = 0
        result_req = []  # Итоговый список запросов, которые мы удовлетворяем
        while i < len(requests):
            target = [0, -1,
                      k + 1]  # [индекс запроса, ценность устройства из этого запроса, кол-во скачанных обновлений у запрашиваемого устройства]
            current_device = requests[i][1]
            while i < len(requests) and requests[i][1] == current_device:
                if importance_devices[current_device][requests[i][0]] > target[1]:
                    target[0] = i
                    target[1] = importance_devices[current_device][requests[i][0]]
                    target[2] = len(devices[requests[i][0]])
                elif importance_devices[current_device][requests[i][0]] == target[1] and len(devices[requests[i][0]]) < \
                        target[2]:
                    target[0] = i
                    target[1] = importance_devices[current_device][requests[i][0]]
                    target[2] = len(devices[requests[i][0]])
                i += 1
            result_req.append(requests[target[0]])

        for i in range(len(result_req)):
            dev1, dev2, upd = result_req[i]
            devices[dev1].add(upd)
            importance_devices[dev1][dev2] += 1
            updates[upd] += 1

        for key in devices:
            if len(devices[key]) == k and check[key] == 0:
                result[key] = timeslot
                check[key] = 1

        timeslot += 1

    return result


timeslots = p2p(n, k)

print(*timeslots[2:])