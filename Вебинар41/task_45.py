def josephus_task(num_people, kill_num):
    """Задача Иосифа Флавия
    :param num_people: количество воинов
    :param kill_num: номер воина
    :return: номер последнего оставшегося воина
    """
    # todo Здесь нужно написать код
    krug = [i for i in range(1, num_people + 1)]
    # print(krug)
    k = kill_num - 1
    while len(krug) > 1:
        if k >= len(krug):
            k = k - len(krug) * (k // len(krug))  # смена счетчика при превышении длины
        krug.pop(k)
        k = k + (kill_num - 1)

        
    return (krug[0])
