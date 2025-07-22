def move_zeros(lst):
    """Перемещение нулей
    :param lst: список из цифр
    :return: список из цифр с нулями в конце
    """
    # todo Здесь нужно написать код
    k = lst.count(0)
    lst1 = list()
    for i in range(1, k + 1):
        lst.remove(0)
        lst1.append(0)
    lst = lst + lst1
    return lst
